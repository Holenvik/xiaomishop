from django.contrib import admin
from articles.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','image','text']
admin.site.register(Article, ArticleAdmin)
