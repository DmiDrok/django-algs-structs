from django.urls import path

from algs import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/<slug:cat_slug>', views.CategoryView.as_view(), name='category'),
    path('categories/<slug:cat_slug>/articles/<slug:article_slug>', views.ArticleView.as_view(), name='article'),
    path('delete/notes', views.DeleteNoteView.as_view(), name='delete_notes'),
]