from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label = 'Имя')
    last_name = forms.CharField(label = 'Фамилия')
    email = forms.EmailField(label = 'Электронная почта')
    address = forms.CharField(label = 'Адрес')
    postal_code = forms.CharField(label = 'Почтовый индекс', max_length=6)
    city = forms.CharField(label = 'Город')
    phone = forms.CharField(label = 'Номер телефона')
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','phone', 'postal_code', 'city']
