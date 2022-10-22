from django import forms
from leasingapp.models import Product

class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username_login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_login'}))


class Register_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'email_register'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'email_register'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_register'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_repeat_register'}))


class Support_form(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['topic'].label = "Запрос на поддержку"
    topic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'topic', 'placeholder': 'Тема запроса/продукт'}))


