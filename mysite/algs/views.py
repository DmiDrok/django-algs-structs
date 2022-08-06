from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView, View
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from algs.models import Article, Category, Note
from algs.utils import DataMixin
from algs.forms import AddNoteForm

import json


# Представление для главной страницы
@method_decorator(cache_page(60), name='dispatch')
class IndexView(DataMixin, ListView):
    template_name = 'algs/index.html'
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_mixin = self.get_user_context(title='Главная страница')
        context.update(c_mixin)

        return context


# Представление для страниц категорий
@method_decorator(cache_page(60*10), name='dispatch')
class CategoryView(DataMixin, ListView):
    template_name = 'algs/categories.html'
    model = Article
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_mixin = self.get_user_context(title='Категории', active_cat=self.kwargs['cat_slug'])
        context.update(c_mixin)

        return context

    def get_queryset(self):
        print(self.kwargs['cat_slug'])
        return Article.objects.filter(category__slug=self.kwargs['cat_slug'])


# Представление для страницы статьи
# @method_decorator(cache_page(60*10), name='dispatch')
class ArticleView(DataMixin, TemplateView):
    template_name = 'algs/article.html'

    def post(self, request, **kwargs):
        print(request.POST)

        Note.objects.create(
            article=Article.objects.get(slug=self.kwargs['article_slug']),
            name=request.POST['name'],
            type=request.POST['type'],
            content=request.POST['content'],
        )

        return redirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_mixin = self.get_user_context(title='Просмотр статьи', active_cat=self.kwargs['cat_slug'], form=AddNoteForm)
        context.update(c_mixin)

        article = Article.objects.get(slug=self.kwargs['article_slug'])
        context['article'] = article
        context['notes'] = Note.objects.filter(article=article)
        article_pk = article.pk

        if article_pk != 1:
            context['prev_art'] = Article.objects.get(pk=article_pk-1)
        
        if article_pk != Article.objects.count():
            context['next_art'] = Article.objects.get(pk=article_pk+1)

        return context


# Представление для удаления заметок
class DeleteNoteView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        del_ids = json.loads(request.body)['del_ids']
        
        for id in del_ids:
            Note.objects.filter(pk=id).delete()

        return HttpResponse('ok')