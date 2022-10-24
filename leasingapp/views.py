from django.shortcuts import render, redirect
import os
from django.http import HttpResponse
from django.template import loader
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from leasingapp.models import *
import pyrebase
from django.core.files.storage import default_storage
from leasingapp.forms import *


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
        Support_Request.objects.create(date=date.today(), topic=request.POST.get('topic'),
                                       name=request.POST.get('name'), phone_num=request.POST.get('phone_num'))
        return render(request, 'support_success_page.html')


def news_page(request):
    news = {'news': Promo.objects.all()}
    return render(request, 'news_page.html', news)


def products_page(request):
    products = {'products': Product.objects.all()}
    return render(request, 'products_page.html', products)


def my_user_account(request): #TODO fix the thing
    # username_form = Change_my_username_form()
    password_form = Change_my_password_form()
    if request.method == 'GET':
        return render(request, 'user_account.html', {'form_password': password_form})
    else:
        user = User.objects.get(id=request.user.id)
        #if request.POST.get('username') != '':
         #   user.username = request.POST.get('username')
        #if request.POST.get('password') != '':
        user.set_password(request.POST.get('password'))

        user.save()
        login(request, user)
        return render(request, 'user_account.html', {'form_password': password_form})



def new_request_add_client(request):
    firebaseConfig = {
        'apiKey': "AIzaSyDZBOo80y_kLGMbeZRbmuB9QtxOoFpZQgE",
        'authDomain': "easy-leasy-33a51.firebaseapp.com",
        'databaseURL': "https://easy-leasy-33a51-default-rtdb.europe-west1.firebasedatabase.app",
        'projectId': "easy-leasy-33a51",
        'storageBucket': "easy-leasy-33a51.appspot.com",
        'messagingSenderId': "614641626422",
        'appId': "1:614641626422:web:921d06880bb4b7172c9797"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    cloud_storage = firebase.storage()
    add_client_form = New_request_add_client_form()
    if request.method == 'GET':
        return render(request, 'new_request_client_data.html', {'form': add_client_form})
    else:
        client_profile = ClientProfile.objects.create(name=request.POST.get('name'), last_name=request.POST.get('last_name'),phone_number=request.POST.get('phone_number'),city=request.POST.get('city'),street=request.POST.get('street'),house_number=request.POST.get('house_num'),
                                                      apartment_number=request.POST.get('apartment_num'),date_of_birth=request.POST.get('date_of_birth'),id_card_num=request.POST.get('id_card_num'),user=request.user)



        income_file = request.FILES['income_proofs']
        file_name = default_storage.save(income_file.name, income_file)#save file to root directory

        income_document = Document.objects.create(definition='income_document', client_profile=client_profile)

        new_income_name = income_document.id.__str__() + '.pdf'

        os.rename(file_name, new_income_name) #rename it to unique id from DB
        cloud_storage.child('/income documents').child(new_income_name).put(new_income_name)
        os.remove(new_income_name)# delete file from root directory after uploading to cloud


        existing_credits_file = request.FILES['existing_credits']
        file_name = default_storage.save(existing_credits_file.name, existing_credits_file)#save file to root directory

        existing_credits_document = Document.objects.create(definition='existing_credits_document', client_profile=client_profile)

        new_existing_credits_name = existing_credits_document.id.__str__() + '.pdf'

        os.rename(file_name, new_existing_credits_name) #rename it to unique id from DB
        cloud_storage.child('/existing credits').child(new_existing_credits_name).put(new_existing_credits_name)
        os.remove(new_existing_credits_name)  # delete file from root directory after uploading to cloud
