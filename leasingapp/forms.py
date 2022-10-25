from django import forms
from leasingapp.models import *


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
        self.fields['name'].label = "Ваше имя"
        self.fields['phone_num'].label = "Номер телефона"

    topic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'topic', 'placeholder': 'Тема запроса/продукт'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'}))
    phone_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_num'}))


class Change_my_username_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Новое имя пользователя"
        self.fields['username'].required = False

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username'}))


class Change_my_password_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = "Новый пароль"
        self.fields['password'].required = False

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'}))


class New_request_add_client_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'last_name'}))
    # citizenship = forms.CharField(widget=forms.TextInput(attrs={'class': 'citizenship'}))
    # sex = forms.CharField(widget=forms.TextInput(attrs={'class': 'sex'}))
    id_card_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'id_card_num'}))
    # id_start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'id_start_date'}))
    # id_end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'id_end_date'}))
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'date_of_birth', 'type': 'date', 'blank': 'true', 'null': 'true'}))
    # marital_status = forms.CharField(widget=forms.TextInput(attrs={'class': 'marital_status'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'city'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'street'}))
    house_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'house_num'}))
    apartment_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'apartment_num'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_number'}))
    income_proofs = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'income_proofs', 'accept': 'application/pdf'}))
    existing_credits = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'existing_credits', 'accept': 'application/pdf'}))
    leasing_object = forms.CharField(widget=forms.TextInput(attrs={'class': 'leasing_object'}))
