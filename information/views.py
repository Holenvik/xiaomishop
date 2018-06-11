from django.shortcuts import render, redirect, get_object_or_404
from xiaomishopapp.models import Category
# Create your views here.

def about(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'information/about.html',
                        {
                        'category': category,
                        'categories': categories,
                        })

def delivery(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'information/delivery.html',
                        {
                        'category': category,
                        'categories': categories,
                        })
def guide(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'information/guide.html',
                        {
                        'category': category,
                        'categories': categories,
                        })
