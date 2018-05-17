from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from xiaomishopapp.forms import UserForm, UserFormForEdit
from .models import Category, Product

from cart.forms import CartAddProductForm

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.






def account(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    user_form = UserFormForEdit(instance=request.user)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'xiaomishop/account.html', {
            'user_form': user_form,
            'username': auth.get_user(request).username, 'category': category,
            'categories': categories,
    } )


def home(request):
    return redirect(xiaomishop_home) # REDIRECT TO def xiaomishop WHERE home.html


def xiaomishop_home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'xiaomishop/home.html', {
            'username': auth.get_user(request).username,
            'category': category,
            'categories': categories,} )



def xiaomishop_sign_up(request):
    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password'],
            ))

            return redirect(xiaomishop_home)

    return render(request, 'xiaomishop/sign_up.html', {
        'user_form': user_form,
    } )

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    paginator = Paginator(products, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)


    return render(request,
                  'xiaomishop/product/list.html',
                  { 'category': category,
                    'categories': categories,
                    'products': products,
                    'username': auth.get_user(request).username,})


def product_detail(request, id, slug, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'xiaomishop/product/detail.html',
                {   'product': product,
                    'username': auth.get_user(request).username,
                    'category': category,
                    'categories': categories,})




def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'xiaomishop/product/detail.html', {
                                                            'product': product,
                                                            'cart_product_form': cart_product_form,
                                                            'categories': categories,})
