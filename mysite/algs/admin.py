from django.contrib import admin

from algs.models import Article, Category, Note


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'publicated']
    list_display_links = ['id', 'title', 'slug']
    list_editable = ['publicated']
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    save_on_top = True


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'article']
    list_display_links = ['id']
    save_on_top = True


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)
