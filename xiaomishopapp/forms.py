from django import forms
from django.contrib.auth.models import User
#from xiaomishopapp.models import Client

class UserForm(forms.ModelForm):
    username = forms.CharField(label = 'Имя пользователя для входа', max_length=100, required = True)
    password = forms.CharField(label = 'Пароль', widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

#class UserFormAdd(forms.ModelForm):
#    class Meta:
#        model = Client
#        fields = ('phone', 'address')

#    def clean_password2(self):
#        cd = self.cleaned_data
    #    if cd['password'] != cd['password2']:
    #        raise forms.ValidationError('Пароль не совпадает!')
    #    return cd['password2']


class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required = True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
