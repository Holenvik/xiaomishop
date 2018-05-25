from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from xiaomishopapp.models import Category


def order_create(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            # запуск асинхронной задачи
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html',
                          {
                          'order': order,
                          'category': category,
                          'categories': categories,
                          })
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {
                  'cart': cart,
                  'form': form,
                  'category': category,
                  'categories': categories,
                  })
