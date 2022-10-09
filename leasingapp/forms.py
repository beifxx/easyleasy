from django import forms

class Login_form(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'lox', 'id':'id2'}))

