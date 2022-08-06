from algs.models import Article, Category

class DataMixin:
    def get_user_context(self, *args, **kwargs):
        context = kwargs
        context['categories'] = Category.objects.all()

        return context