from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from leasingapp.models import Promo, Product, Support_Request, ClientProfile

from leasingapp.forms import Login_form, Register_form, Support_form


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
        try:
            User.objects.get(username=username)
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
    # news = Promo.objects.
    home_content = {'product': Product.objects.first(), 'news': Promo.objects.first()}
    return render(request, 'home_page_user.html', home_content)


def product_page(request, product_id):
    product = {'product': Product.objects.get(id=product_id)}
    return render(request, 'product_page.html', product)


def support_page(request):
    if request.method == 'GET':
        form = Support_form()
        return render(request, 'support_request.html', {'form': form})
    else:
        client_profile = ClientProfile.objects.filter(user=request.user).first()
        Support_Request.objects.create(date=date.today(), topic=request.POST.get('topic'),
                                       client_profile=client_profile)
        return render(request, 'support_success_page.html')


def news_page(request):
    news = {'news': Promo.objects.all()}
    return render(request, 'news_page.html', news)


def products_page(request):
    products = {'products': Product.objects.all()}
    return render(request, 'products_page.html', products)