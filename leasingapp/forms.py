from django import forms


class Login_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username_login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_login'}))


class Register_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'email_register'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'email_register'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_register'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password_repeat_register'}))
