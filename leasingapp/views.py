from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from leasingapp.models import Promo, Product

from leasingapp.forms import Login_form, Register_form


def login_page(request):
    form = Login_form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # try:
        #   User.objects.get(email=email)
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff == 1:
                return redirect('a/home')
            else:
                return redirect('u/home')
    else:
        return render(request, "login_page.html", {'form': form})


def register_page(request):
    form = Register_form
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username)
        print(password)
        try: User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            if user.is_staff == 1:
                return redirect('a/home')
            else:
                return redirect('u/home')


    else:
        return render(request, "register_page.html", {'form': form})


def home_page(request):
    #news = Promo.objects.
    home_content = {'product': Product.objects.first(), 'news': Promo.objects.first()}
    return render(request, 'home_page_user.html', home_content)

def product_page(request, product_id):
    product = {'product': Product.objects.get(id=product_id)}
    return render(request, 'product_page.html', product)

