from django.shortcuts import render, redirect, get_object_or_404
from articles.models import Article
from xiaomishopapp.models import Category
# Create your views here.

def article(request, slug, category_slug=None):
    article = get_object_or_404(Article,
                                slug=slug,
                                )
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'article/article.html',
                  {
                    'article': article,
                    'category': category,
                    'categories': categories,
                    })
