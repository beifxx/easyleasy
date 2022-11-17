import smtplib, ssl
import os
import zipfile
from datetime import date, datetime

import firebase_admin
import numpy
import pyrebase
from dateutil.relativedelta import relativedelta
from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
from django.db.models import Avg
from django.http import FileResponse
from django.shortcuts import render, redirect
from firebase_admin import credentials

from leasingapp.forms import *

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
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "easy-leasy-33a51",
    "private_key_id": "343efe54dfe2076bbfbcbde2820fa0148ba1d697",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQChTNqIoyd/8CFU\ndFStqwo96xSDIe+frpjrYUoAaRMqw+oBDvv1MeN2pnU+8ytW8jPxKDLJkKABJjXd\nZFJaDB8c22po/NyR9r2nt8A1hw9CCKd5naHFcA2e8tlbLmpKCe8+Myz5MhTRJK1p\n4t0M9dUXj2zhwYfvlg7ngvcefdcxHP9y8ZdMcVeEZ5Ql5Lv0GrnYuFPDwMjpqtWV\nZsDqHrTksjYKOb8CdBX0+6Z5I+DS9myzYZuaM+hijNzw4XXZw/CPRlIQXbss45A6\naMHZ6QBabPLKI3UcPsfzvvZv6ig2EihS2RLgbON7FncZtxKkHqTe/mi+06qkcrsk\nKHM3DNFRAgMBAAECggEABz8iVknWMsuWrmpSNOyJQkI3IrO58JecgSlWyhvuY4PN\nFeJsHsDwsi+aTDYKjWvGOksPCmU3+wqSGEczN/PGy2TELBaoJi/1Uf1Rt6tAsTvI\nTRDFks7iSHDVTmEQdLvA3C+FEWZW7xUnFqm9j/Z/bgE16BKUyTEZrFGtnoNoJpRP\nq/PzC40JtNAof5Thu0auOe2Z+E6fJXOlsfBOgAHfW67pFUjYWQaPWS/4bZyfdguh\naxW9X/Ef8h9RdurjN08LOiX7WpJ5lWnAwU8JY8mH5LpfmW4TD2gMIUJ5t63s6bY0\nwXRXCwWRg45zJh6wioPfEsFBxnw96Vz8aSw2C9cxPQKBgQDO+Pvj1mz4+4WGLP12\niWc5yzhGpSNrz05C+k2GLv/q/pxc8LHYPq/1nSbWmm7CwVHWtt3BznYET2uFnZWZ\nUMUKN4e8mRZAadzx/BXb/aQ7LPOOJGWMPCOcUnaR7lZZmg47hS1H6vZIWqajHb1S\nh9dVYQ7A5YA3iMZWHOZCxj2YywKBgQDHgkCtnv2ffy+OET6RP+M4H7dM3AUjetyE\nNW3C64vRJ2q6ctTSv823Roe5RWqCyDGo9ysnd4iwdwJO3v0xLNavDpM9oW8r8J1X\nDsg3FXyH4v7ixCTBAxQNWIrwEjNjwSkCtullDguHLROELPg3AblVWZBQ5UtM0/OJ\nYyLXJFVm0wKBgQClAskAWwJCd3V7Bf+GNAICh8z0NdDJsVu59ok8Q9hxaFENoDCK\nMWBkN8ixLCrGRw6SWvTuAUcCJLearYqJ02VkweUMLhkZfc1TeCGNZOk87Je5abc0\nWPYjOXOi4RwjD7ntJj51qhR0lyFnxtwcIoVBYsI6dD8HB5rpKN1Du318hQKBgCP3\nqH9khWbGwCUFmNkIwobwuNQDam2+DZlMJJCadGdtisE4SIQCDi03auqMyCnxu3ox\nrTb9RshBfEoJy22dHssKfqMCwo8SXts+D/xWRFAfLUJmiBW/31KUnt+u+FLIlQMn\nRKZyRMPG7ZjLnqgUCHyJnAnpfIzKPUKMe9B7fWX/AoGANBoofs8bAvD70r2vparl\nZlrL/lm0fqyQ7cExD/YsdxS235mHQFa1nyLgjTovvLe42XARJ6cbqCcH09+12D16\nRaESv8FA0CzQYMaoeZsoc7xLIPhcx7JE8/3cq2aa2qcKhT9VsLqI/j9d6BghMJlk\nxdh/woJoomS0SdvIZX1OpvA=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-x78xi@easy-leasy-33a51.iam.gserviceaccount.com",
    "client_id": "115483754411798145818",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-x78xi%40easy-leasy-33a51.iam.gserviceaccount.com"
}
)
firebase_admin.initialize_app(cred)


def login_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))

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
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))

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


def user_home_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    # news = Promo.objects.
    home_content = {'product': Product.objects.first(), 'news': Promo.objects.first()}
    return render(request, 'home_page_user.html', home_content)


def admin_home_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    return render(request, 'home_page_admin.html')


def product_page(request, product_id):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    product = {'product': Product.objects.get(id=product_id)}
    return render(request, 'product_page.html', product)


def support_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    if request.method == 'GET':
        form = Support_form()
        return render(request, 'support_request.html', {'form': form})
    else:
        Support_Request.objects.create(date=date.today(), topic=request.POST.get('topic'),
                                       name=request.POST.get('name'), phone_num=request.POST.get('phone_num'))
        return render(request, 'support_success_page.html')


def news_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    news = {'news': Promo.objects.all()}
    return render(request, 'news_page.html', news)


def products_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    products = {'products': Product.objects.all()}
    return render(request, 'products_page.html', products)


def my_user_account(request):  # TODO fix the thing
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    # username_form = Change_my_username_form()
    password_form = Change_my_password_form()
    if request.method == 'GET':
        applications = Application.objects.filter(client_profile__user=request.user)
        deeds = Deal.objects.filter(client_profile__user=request.user)
        return render(request, 'user_account.html',
                      {'form_password': password_form, 'applications': applications, 'deeds': deeds})
    else:
        user = User.objects.get(id=request.user.id)
        # if request.POST.get('username') != '':
        #   user.username = request.POST.get('username')
        # if request.POST.get('password') != '':
        user.set_password(request.POST.get('password'))

        user.save()
        login(request, user)
        return render(request, 'user_account.html', {'form_password': password_form})


def new_request_choose_type(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    return render(request, "choose_leasing_type.html")


def phys_new_request(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    new_request_form = New_request_phys_form()
    products = Product.objects.all()
    if request.method == 'GET':
        return render(request, 'new_request_client_data.html', {'form': new_request_form, 'products': products})
    else:
        client_profile = ClientProfile.objects.create(name=request.POST.get('name'),
                                                      last_name=request.POST.get('last_name'),
                                                      phone_number=request.POST.get('phone_number'), type="Физлицо",
                                                      user=request.user)
        ######################################################
        income_file = request.FILES['income']
        file_name = default_storage.save(income_file.name, income_file)  # save file to root directory

        income_document = Document.objects.create(definition='income_document', client_profile=client_profile)

        new_income_name = income_document.id.__str__() + '.pdf'

        os.rename(file_name, new_income_name)  # rename it to unique id from DB
        cloud_storage.child('/phys').child('income').child(new_income_name).put(new_income_name)
        os.remove(new_income_name)  # delete file from root directory after uploading to cloud

        ######################################################
        existing_credits_file = request.FILES['existing_credits']
        file_name = default_storage.save(existing_credits_file.name,
                                         existing_credits_file)  # save file to root directory

        existing_credits_document = Document.objects.create(definition='existing_credits_document',
                                                            client_profile=client_profile)

        new_existing_credits_name = existing_credits_document.id.__str__() + '.pdf'

        os.rename(file_name, new_existing_credits_name)  # rename it to unique id from DB
        cloud_storage.child('/phys').child('existing_credits').child(new_existing_credits_name).put(
            new_existing_credits_name)
        os.remove(new_existing_credits_name)  # delete file from root directory after uploading to cloud

        ######################################################
        leasing_object_file = request.FILES['leasing_object']
        file_name = default_storage.save(leasing_object_file.name, leasing_object_file)  # save file to root directory

        leasing_object_document = Document.objects.create(definition='leasing_object_document',
                                                          client_profile=client_profile)

        new_leasing_object_name = leasing_object_document.id.__str__() + '.pdf'

        os.rename(file_name, new_leasing_object_name)  # rename it to unique id from DB
        cloud_storage.child('/phys').child('leasing_object').child(new_leasing_object_name).put(new_leasing_object_name)
        os.remove(new_leasing_object_name)  # delete file from root directory after uploading to cloud
        ######################################################
        application_file = request.FILES['application']
        file_name = default_storage.save(application_file.name, application_file)  # save file to root directory

        application_document = Document.objects.create(definition='application_document', client_profile=client_profile)

        new_application_name = application_document.id.__str__() + '.pdf'

        os.rename(file_name, new_application_name)  # rename it to unique id from DB
        cloud_storage.child('/phys').child('application').child(new_application_name).put(new_application_name)
        os.remove(new_application_name)  # delete file from root directory after uploading to cloud
        ######################################################
        credit_report_agreement_file = request.FILES['credit_report_agreement']
        file_name = default_storage.save(credit_report_agreement_file.name,
                                         credit_report_agreement_file)  # save file to root directory

        credit_report_agreement_document = Document.objects.create(definition='credit_report_agreement_document',
                                                                   client_profile=client_profile)

        new_credit_report_agreement_name = credit_report_agreement_document.id.__str__() + '.pdf'

        os.rename(file_name, new_credit_report_agreement_name)  # rename it to unique id from DB
        cloud_storage.child('/phys').child('credit_report_agreement').child(new_credit_report_agreement_name).put(
            new_credit_report_agreement_name)
        os.remove(new_credit_report_agreement_name)  # delete file from root directory after uploading to cloud
        ######################################################
        passport_file = request.FILES['passport']
        file_name = default_storage.save(passport_file.name, passport_file)  # save file to root directory

        passport_document = Document.objects.create(definition='passport_document', client_profile=client_profile)

        new_passport_name = passport_document.id.__str__() + '.pdf'

        os.rename(file_name, new_passport_name)  # rename it to unique id from DB
        cloud_storage.child('/phys').child('passport').child(new_passport_name).put(new_passport_name)
        os.remove(new_passport_name)  # delete file from root directory after uploading to cloud
        ######################################################
        work_record_book_file = request.FILES['work_record_book']
        file_name = default_storage.save(work_record_book_file.name,
                                         work_record_book_file)  # save file to root directory

        work_record_book_document = Document.objects.create(definition='work_record_book_document',
                                                            client_profile=client_profile)

        new_work_record_book_name = work_record_book_document.id.__str__() + '.pdf'

        os.rename(file_name, new_work_record_book_name)  # rename it to unique id from DB
        cloud_storage.child('/phys').child('work_record_book').child(new_work_record_book_name).put(
            new_work_record_book_name)
        os.remove(new_work_record_book_name)  # delete file from root directory after uploading to cloud
        ######################################################
        Application.objects.create(date_applied=date.today(), client_profile=client_profile,
                                   product_id=request.POST.get('product_id'), status="В обработке")
        return render(request, 'application_success.html')


def jur_new_request(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    new_request_form = New_request_jur_form()
    products = Product.objects.all()
    if request.method == 'GET':
        return render(request, 'new_request_client_data.html', {'form': new_request_form, 'products': products})
    else:
        client_profile = ClientProfile.objects.create(name=request.POST.get('name'),
                                                      last_name=request.POST.get('last_name'),
                                                      phone_number=request.POST.get('phone_number'), type="Юрлицо",
                                                      user=request.user)
        ######################################################

        annual_financial_reporting_file = request.FILES['annual_financial_reporting']
        file_name = default_storage.save(annual_financial_reporting_file.name,
                                         annual_financial_reporting_file)  # save file to root directory

        annual_financial_reporting_document = Document.objects.create(definition='annual_financial_reporting_document',
                                                                      client_profile=client_profile)

        new_annual_financial_reporting_name = annual_financial_reporting_document.id.__str__() + '.pdf'

        os.rename(file_name, new_annual_financial_reporting_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('annual_financial_reporting').child(new_annual_financial_reporting_name).put(
            new_annual_financial_reporting_name)
        os.remove(new_annual_financial_reporting_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        bank_extract_file = request.FILES['bank_extract']
        file_name = default_storage.save(bank_extract_file.name, bank_extract_file)  # save file to root directory

        bank_extract_document = Document.objects.create(definition='bank_extract_document',
                                                        client_profile=client_profile)

        new_bank_extract_name = bank_extract_document.id.__str__() + '.pdf'

        os.rename(file_name, new_bank_extract_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('bank_extract').child(new_bank_extract_name).put(new_bank_extract_name)
        os.remove(new_bank_extract_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        leasing_object_file = request.FILES['leasing_object']
        file_name = default_storage.save(leasing_object_file.name, leasing_object_file)  # save file to root directory

        leasing_object_document = Document.objects.create(definition='leasing_object_document',
                                                          client_profile=client_profile)

        new_leasing_object_name = leasing_object_document.id.__str__() + '.pdf'

        os.rename(file_name, new_leasing_object_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('leasing_object').child(new_leasing_object_name).put(new_leasing_object_name)
        os.remove(new_leasing_object_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        application_file = request.FILES['application']
        file_name = default_storage.save(application_file.name, application_file)  # save file to root directory

        application_document = Document.objects.create(definition='application_document', client_profile=client_profile)

        new_application_name = application_document.id.__str__() + '.pdf'

        os.rename(file_name, new_application_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('application').child(new_application_name).put(new_application_name)
        os.remove(new_application_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        chief_officer_assignment_file = request.FILES['chief_officer_assignment']
        file_name = default_storage.save(chief_officer_assignment_file.name,
                                         chief_officer_assignment_file)  # save file to root directory

        chief_officer_assignment_document = Document.objects.create(definition='chief_officer_assignment_document',
                                                                    client_profile=client_profile)

        new_chief_officer_assignment_name = chief_officer_assignment_document.id.__str__() + '.pdf'

        os.rename(file_name, new_chief_officer_assignment_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('chief_officer_assignment').child(new_chief_officer_assignment_name).put(
            new_chief_officer_assignment_name)
        os.remove(new_chief_officer_assignment_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        chief_officer_id_file = request.FILES['chief_officer_id']
        file_name = default_storage.save(chief_officer_id_file.name,
                                         chief_officer_id_file)  # save file to root directory

        chief_officer_id_document = Document.objects.create(definition='chief_officer_id_document',
                                                            client_profile=client_profile)

        new_chief_officer_id_name = chief_officer_id_document.id.__str__() + '.pdf'

        os.rename(file_name, new_chief_officer_id_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('chief_officer_id').child(new_chief_officer_id_name).put(
            new_chief_officer_id_name)
        os.remove(new_chief_officer_id_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        debit_credit_debt_file = request.FILES['debit_credit_debt']
        file_name = default_storage.save(debit_credit_debt_file.name,
                                         debit_credit_debt_file)  # save file to root directory

        debit_credit_debt_document = Document.objects.create(definition='debit_credit_debt_document',
                                                             client_profile=client_profile)

        new_debit_credit_debt_name = debit_credit_debt_document.id.__str__() + '.pdf'

        os.rename(file_name, new_debit_credit_debt_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('debit_credit_debt').child(new_debit_credit_debt_name).put(
            new_debit_credit_debt_name)
        os.remove(new_debit_credit_debt_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        creditor_debitor_debt_file = request.FILES['creditor_debitor_debt']
        file_name = default_storage.save(creditor_debitor_debt_file.name,
                                         creditor_debitor_debt_file)  # save file to root directory

        creditor_debitor_debt_document = Document.objects.create(definition='creditor_debitor_debt_document',
                                                                 client_profile=client_profile)

        new_creditor_debitor_debt_name = creditor_debitor_debt_document.id.__str__() + '.pdf'

        os.rename(file_name, new_creditor_debitor_debt_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('creditor_debitor_debt').child(new_creditor_debitor_debt_name).put(
            new_creditor_debitor_debt_name)
        os.remove(new_creditor_debitor_debt_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        entity_statute_file = request.FILES['entity_statute']
        file_name = default_storage.save(entity_statute_file.name, entity_statute_file)  # save file to root directory

        entity_statute_document = Document.objects.create(definition='entity_statute_document',
                                                          client_profile=client_profile)

        new_entity_statute_name = entity_statute_document.id.__str__() + '.pdf'

        os.rename(file_name, new_entity_statute_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('entity_statute').child(new_entity_statute_name).put(new_entity_statute_name)
        os.remove(new_entity_statute_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        equipment_list_file = request.FILES['equipment_list']
        file_name = default_storage.save(equipment_list_file.name, equipment_list_file)  # save file to root directory

        equipment_list_document = Document.objects.create(definition='equipment_list_document',
                                                          client_profile=client_profile)

        new_equipment_list_name = equipment_list_document.id.__str__() + '.pdf'

        os.rename(file_name, new_equipment_list_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('equipment_list').child(new_equipment_list_name).put(new_equipment_list_name)
        os.remove(new_equipment_list_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        interim_financial_reporting_file = request.FILES['interim_financial_reporting']
        file_name = default_storage.save(interim_financial_reporting_file.name,
                                         interim_financial_reporting_file)  # save file to root directory

        interim_financial_reporting_document = Document.objects.create(
            definition='interim_financial_reporting_document', client_profile=client_profile)

        new_interim_financial_reporting_name = interim_financial_reporting_document.id.__str__() + '.pdf'

        os.rename(file_name, new_interim_financial_reporting_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('interim_financial_reporting').child(
            new_interim_financial_reporting_name).put(new_interim_financial_reporting_name)
        os.remove(new_interim_financial_reporting_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        existing_credits_file = request.FILES['existing_credits']
        file_name = default_storage.save(existing_credits_file.name,
                                         existing_credits_file)  # save file to root directory

        existing_credits_document = Document.objects.create(definition='existing_credits_document',
                                                            client_profile=client_profile)

        new_existing_credits_name = existing_credits_document.id.__str__() + '.pdf'

        os.rename(file_name, new_existing_credits_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('existing_credits').child(new_existing_credits_name).put(
            new_existing_credits_name)
        os.remove(new_existing_credits_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        license_file = request.FILES['license']
        file_name = default_storage.save(license_file.name, license_file)  # save file to root directory

        license_document = Document.objects.create(definition='license_document', client_profile=client_profile)

        new_license_name = license_document.id.__str__() + '.pdf'

        os.rename(file_name, new_license_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('license').child(new_license_name).put(new_license_name)
        os.remove(new_license_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        object_usage_file = request.FILES['object_usage']
        file_name = default_storage.save(object_usage_file.name, object_usage_file)  # save file to root directory

        object_usage_document = Document.objects.create(definition='object_usage_document',
                                                        client_profile=client_profile)

        new_object_usage_name = object_usage_document.id.__str__() + '.pdf'

        os.rename(file_name, new_object_usage_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('object_usage').child(new_object_usage_name).put(new_object_usage_name)
        os.remove(new_object_usage_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        registration_file = request.FILES['registration']
        file_name = default_storage.save(registration_file.name, registration_file)  # save file to root directory

        registration_document = Document.objects.create(definition='registration_document',
                                                        client_profile=client_profile)

        new_registration_name = registration_document.id.__str__() + '.pdf'

        os.rename(file_name, new_registration_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('registration').child(new_registration_name).put(new_registration_name)
        os.remove(new_registration_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        if request.FILES['shareholder_registration'] is not None:
            shareholder_registration_file = request.FILES['shareholder_registration']
            file_name = default_storage.save(shareholder_registration_file.name,
                                             shareholder_registration_file)  # save file to root directory

            shareholder_registration_document = Document.objects.create(definition='shareholder_registration_document',
                                                                        client_profile=client_profile)

            new_shareholder_registration_name = shareholder_registration_document.id.__str__() + '.pdf'

            os.rename(file_name, new_shareholder_registration_name)  # rename it to unique id from DB
            cloud_storage.child('/jur').child('shareholder_registration').child(new_shareholder_registration_name).put(
                new_shareholder_registration_name)
            os.remove(new_shareholder_registration_name)  # delete file from root directory after uploading to cloud

        ######################################################        ######################################################
        tax_statement_file = request.FILES['tax_statement']
        file_name = default_storage.save(tax_statement_file.name, tax_statement_file)  # save file to root directory

        tax_statement_document = Document.objects.create(definition='tax_statement_document',
                                                         client_profile=client_profile)

        new_tax_statement_name = tax_statement_document.id.__str__() + '.pdf'

        os.rename(file_name, new_tax_statement_name)  # rename it to unique id from DB
        cloud_storage.child('/jur').child('tax_statement').child(new_tax_statement_name).put(new_tax_statement_name)
        os.remove(new_tax_statement_name)  # delete file from root directory after uploading to cloud

        ######################################################
        Application.objects.create(date_applied=date.today(), client_profile=client_profile,
                                   product_id=request.POST.get('product_id'), status="В обработке")
        return render(request, 'application_success.html')


def admin_applications_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    applications = Application.objects.all()
    return render(request, 'admin_applications.html', {'applications': applications})


def admin_single_application(request, application_id):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    application = Application.objects.get(id=application_id)
    if request.method == 'GET':

        form = Admin_application_form()
        if application.client_profile.type == "Физлицо":
            downloadl_link = "/a/phys/download"
        else:
            downloadl_link = "/a/jur/download"
        return render(request, 'admin_single_application_page.html',
                      {'application': application, 'form': form, 'download_link': downloadl_link})
    else:
        if request.POST.get('accept') is not None:
            application.status = "Одобрена"
            application.save()
            if Deal.objects.filter(client_profile=application.client_profile).exists():
                deed = Deal.objects.get(client_profile=application.client_profile)
                deed.duration = request.POST.get('duration')
                deed.rate = request.POST.get('rate')
                deed.loan_amount = request.POST.get('loan_amount')
                deed.regular_payment_size = request.POST.get('loan_amount')
                deed.status = "В анализе"
                deed.product = application.product
                deed.save()
            else:
                deed = Deal.objects.create(duration=request.POST.get('duration'),
                                           rate=request.POST.get('rate'),
                                           loan_amount=request.POST.get('loan_amount'),
                                           regular_payment_size=request.POST.get('loan_amount'),
                                           status="В анализе",
                                           client_profile=application.client_profile,
                                           product=application.product)
            return render(request, 'admin_single_deed_page.html', {'deed': deed})
        else:
            application.status = "Отклонена"
            application.save()
            return render(request, 'admin_applications.html')


def download_phys_zip(request):
    income_file_name = "Данные о доходах.pdf"
    existing_credits_file_name = "Данные о текущих кредитах.pdf"
    leasing_object_file_name = "Данные об объекте лизинга.pdf"
    application_file_name = "Заявление.pdf"
    credit_report_agreement_file_name = "Согласие на предоставление кредитного отчета.pdf"
    passport_file_name = "Паспорт.pdf"
    work_record_book_file_name = "Трудовая книжка.pdf"
    income = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                     definition="income_document").first()
    existing_credits = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                               definition="existing_credits_document").first()
    leasing_object = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                             definition="leasing_object_document").first()
    application = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                          definition="application_document").first()
    credit_report_agreement = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                                      definition="credit_report_agreement_document").first()
    passport = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                       definition="passport_document").first()
    work_record_book = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                               definition="work_record_book_document").first()

    cloud_storage.child('/phys/income/' + income.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/phys/income', filename=income_file_name)
    cloud_storage.child('/phys/existing_credits/' + existing_credits.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/phys/existing_credits', filename=existing_credits_file_name)
    cloud_storage.child('/phys/leasing_object/' + leasing_object.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/phys/leasing_object', filename=leasing_object_file_name)
    cloud_storage.child('/phys/application/' + application.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/phys/application', filename=application_file_name)
    cloud_storage.child('/phys/credit_report_agreement/' + credit_report_agreement.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/phys/credit_report_agreement', filename=credit_report_agreement_file_name)
    cloud_storage.child('/phys/passport/' + passport.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/phys/passport', filename=passport_file_name)
    cloud_storage.child('/phys/work_record_book/' + work_record_book.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/phys/work_record_book', filename=work_record_book_file_name)

    zip_name = 'zip_file.zip'
    z = zipfile.ZipFile(zip_name, 'w')

    z.write(income_file_name)
    z.write(existing_credits_file_name)
    z.write(leasing_object_file_name)
    z.write(application_file_name)
    z.write(credit_report_agreement_file_name)
    z.write(passport_file_name)
    z.write(work_record_book_file_name)
    z.close()

    return FileResponse(
        open(zip_name, 'rb'),
        as_attachment=True,
        filename='Архив документов клиента.zip'
    )


def download_jur_zip(request):
    print("JURY TIIIIIIIIIMEEEEEE")

    annual_financial_reporting_file_name = "Годовая Финансовая отчетность, с отметкой ИМНС, за последние два (2) года.pdf"
    bank_extract_file_name = "Справка банка, в котором обслуживается Клиент.pdf"
    leasing_object_file_name = "Детальная информация об объекте лизинга.pdf"
    application_file_name = "Заявление на заключение договора лизинга.pdf"
    chief_officer_assignment_file_name = "Копия документов, подтверждающая факт назначения и полномочия генерального директора.pdf"
    chief_officer_id_file_name = "Копия паспорта директора.pdf"
    debit_credit_debt_file_name = "Расшифровка задолженности по кредитам, займам, лизинговым договорам на последнюю отчетную дату с указанием сроков погашения.pdf"
    creditor_debitor_debt_file_name = "Расшифровка дебиторской и кредиторской задолженности на последнюю отчетную дату в разрезе сроков образования.pdf"
    entity_statute_file_name = "Копия Устава со всеми изменениями и дополнениями.pdf"
    equipment_list_file_name = "Опись основных средств с указанием остаточной балансовой стоимости на последнюю отчетную дату.pdf"
    interim_financial_reporting_file_name = "Промежуточная Финансовая отчетность за последний отчетный период.pdf"
    existing_credits_file_name = "Копии действующих кредитных, факторинговых и лизинговых договоров.pdf"
    license_file_name = "Имеющиеся лицензии.pdf"
    object_usage_file_name = "Общая информация о компании и об использовании объекта лизинга.pdf"
    registration_file_name = "Копия свидетельства о регистрации.pdf"
    shareholder_registration_file_name = "Выписка из реестра акционеров (при наличии).pdf"
    tax_statement_file_name = "Копия свидетельства о постановке на налоговый учет в ИМНС.pdf"
    annual_financial_reporting = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                                         definition="annual_financial_reporting_document").first()
    existing_credits = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                               definition="existing_credits_document").first()
    leasing_object = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                             definition="leasing_object_document").first()
    application = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                          definition="application_document").first()
    bank_extract = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                           definition="bank_extract_document").first()
    chief_officer_assignment = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                                       definition="chief_officer_assignment_document").first()
    chief_officer_id = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                               definition="chief_officer_id_document").first()
    debit_credit_debt = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                                definition="debit_credit_debt_document").first()
    creditor_debitor_debt = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                                    definition="creditor_debitor_debt_document").first()
    entity_statute = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                             definition="entity_statute_document").first()
    equipment_list = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                             definition="equipment_list_document").first()
    interim_financial_reporting = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                                          definition="interim_financial_reporting_document").first()
    license_custom = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                             definition="license_document").first()
    object_usage = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                           definition="object_usage_document").first()
    registration = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                           definition="registration_document").first()
    shareholder_registration = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                                       definition="shareholder_registration_document").first()
    tax_statement = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                            definition="tax_statement_document").first()

    cloud_storage.child('/jur/annual_financial_reporting/' + annual_financial_reporting.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/annual_financial_reporting',
        filename=annual_financial_reporting_file_name)
    cloud_storage.child('/jur/existing_credits/' + existing_credits.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/existing_credits', filename=existing_credits_file_name)
    cloud_storage.child('/jur/leasing_object/' + leasing_object.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/leasing_object', filename=leasing_object_file_name)
    cloud_storage.child('/jur/application/' + application.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/application', filename=application_file_name)
    cloud_storage.child('/jur/bank_extract/' + bank_extract.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/bank_extract', filename=bank_extract_file_name)
    cloud_storage.child('/jur/chief_officer_assignment/' + chief_officer_assignment.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/chief_officer_assignment', filename=chief_officer_assignment_file_name)
    cloud_storage.child('/jur/chief_officer_id/' + chief_officer_id.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/chief_officer_id', filename=chief_officer_id_file_name)
    cloud_storage.child('/jur/debit_credit_debt/' + debit_credit_debt.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/debit_credit_debt', filename=debit_credit_debt_file_name)
    cloud_storage.child('/jur/creditor_debitor_debt/' + creditor_debitor_debt.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/creditor_debitor_debt', filename=creditor_debitor_debt_file_name)
    cloud_storage.child('/jur/entity_statute/' + entity_statute.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/entity_statute', filename=entity_statute_file_name)
    cloud_storage.child('/jur/equipment_list/' + equipment_list.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/equipment_list', filename=equipment_list_file_name)
    cloud_storage.child(
        '/jur/interim_financial_reporting/' + interim_financial_reporting.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/interim_financial_reporting',
        filename=interim_financial_reporting_file_name)
    cloud_storage.child('/jur/license/' + license_custom.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/license', filename=license_file_name)
    cloud_storage.child('/jur/object_usage/' + object_usage.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/object_usage', filename=object_usage_file_name)
    cloud_storage.child('/jur/registration/' + registration.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/registration', filename=registration_file_name)
    cloud_storage.child('/jur/shareholder_registration/' + shareholder_registration.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/shareholder_registration', filename=shareholder_registration_file_name)
    cloud_storage.child('/jur/tax_statement/' + tax_statement.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/jur/tax_statement', filename=tax_statement_file_name)

    zip_name = 'zip_file.zip'
    z = zipfile.ZipFile(zip_name, 'w')

    z.write(annual_financial_reporting_file_name)
    z.write(bank_extract_file_name)
    z.write(leasing_object_file_name)
    z.write(application_file_name)
    z.write(chief_officer_assignment_file_name)
    z.write(chief_officer_id_file_name)
    z.write(debit_credit_debt_file_name)
    z.write(creditor_debitor_debt_file_name)
    z.write(entity_statute_file_name)
    z.write(equipment_list_file_name)
    z.write(interim_financial_reporting_file_name)
    z.write(existing_credits_file_name)
    z.write(license_file_name)
    z.write(object_usage_file_name)
    z.write(registration_file_name)
    z.write(shareholder_registration_file_name)
    z.write(tax_statement_file_name)

    z.close()

    return FileResponse(
        open(zip_name, 'rb'),
        as_attachment=True,
        filename='Архив документов клиента.zip'
    )


def support_requests_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    if request.method == 'GET':
        support_requests = Support_Request.objects.all()
        return render(request, 'admin_support_requests_page.html', {'support_requests': support_requests})
    else:
        request_delete = Support_Request.objects.get(id=request.POST.get('request_id'))
        request_delete.delete()
        support_requests = Support_Request.objects.all()
        return render(request, 'admin_support_requests_page.html', {'support_requests': support_requests})


def deeds_page(request):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    deeds = Deal.objects.all()
    return render(request, 'admin_deeds_page.html', {'deeds': deeds})


def admin_single_deed(request, deed_id):
    for parent, dirnames, filenames in os.walk('../easyleasy'):
        for fn in filenames:
            if fn.lower().endswith('.pdf'):
                os.remove(os.path.join(parent, fn))
    deed = Deal.objects.get(client_profile_id=deed_id)
    if request.method == 'GET':
        form = Admin_deed_form()
        if deed.client_profile.type == "Физлицо":
            downloadl_link = "/a/phys/download"
        else:
            downloadl_link = "/a/jur/download"
        return render(request, 'admin_single_deed_page.html',
                      {'deed': deed, 'form': form, 'download_link': downloadl_link})
    if request.method == 'POST':
        if request.POST.get('duration') != '':
            deed.duration = request.POST.get('duration')
        if request.POST.get('rate') != '':
            deed.rate = request.POST.get('rate')
        if request.POST.get('loan_amount') != '':
            deed.loan_amount = request.POST.get('loan_amount')
        if request.POST.get('regular_payment_size') != '':
            deed.regular_payment_size = request.POST.get('regular_payment_size')
        if request.POST.get('date_signed') != '':
            deed.date_signed = request.POST.get('date_signed')
        deed.status = request.POST.get('status_update')
        if request.FILES.get('contract', False) is not False:
            contract_file = request.FILES['contract']
            file_name = default_storage.save(contract_file.name,
                                             contract_file)  # save file to root directory

            if Document.objects.filter(client_profile=deed.client_profile, definition='contract').exists():
                contract_document = Document.objects.get(client_profile=deed.client_profile, definition='contract')
                contract_name = contract_document.id.__str__() + '.pdf'

                os.rename(file_name, contract_name)  # rename it to unique id from DB
                cloud_storage.child('/contract').child(contract_name).put(contract_name)
                deed.contract = contract_document
            else:
                contract_document = Document.objects.create(definition='contract',
                                                            client_profile=deed.client_profile)
                contract_name = contract_document.id.__str__() + '.pdf'

                os.rename(file_name, contract_name)  # rename it to unique id from DB
                cloud_storage.child('/contract').child(contract_name).put(
                    contract_name)
                deed.contract = contract_document
                os.remove(contract_name)  # delete file from root directory after uploading to cloud
        deed.save()
        request.method = 'GET'
        return admin_single_deed(request, deed_id)


def download_contract(request):
    contract_name = "Копия договора.pdf"

    contract = Document.objects.filter(client_profile_id=request.POST.get('client_profile'),
                                       definition="contract").first()

    cloud_storage.child('/contract/' + contract.id.__str__() + '.pdf').download(
        'gs://easy-leasy-33a51.appspot.com/contract', filename=contract_name)

    return FileResponse(
        open(contract_name, 'rb'),
        as_attachment=True,
        filename='Копия договора.pdf'
    )


def admin_stats(request):
    clients = ClientProfile.objects.all()
    jur_part = (ClientProfile.objects.filter(type='Физлицо').count() * 100 / clients.count()).__trunc__()
    phys_part = 100 - jur_part

    av_loan_amount = Deal.objects.all().aggregate(Avg('loan_amount'))
    av_duration = Deal.objects.all().aggregate(Avg('duration'))

    deals = Deal.objects.all()
    immovable_part = (Deal.objects.filter(product__type="Недвижимость").count() * 100 / deals.count()).__trunc__()

    equipment_part = (Deal.objects.filter(product__type="Оборудование").count() * 100 / deals.count()).__trunc__()

    transport_part = (Deal.objects.filter(product__type="Транспорт").count() * 100 / deals.count()).__trunc__()

    return render(request, 'admin_stats.html',
                  {'jur_part': jur_part, 'phys_part': phys_part, 'av_loan_amount': av_loan_amount,
                   'av_duration': av_duration,
                   'transport_part': transport_part, 'equipment_part': equipment_part,
                   'immovable_part': immovable_part})


def get_mail(request):
    port = 465  # For SSL
    password = 'dmfmphoqyckhcmjg'
    user_email = request.user.email
    deed = Deal.objects.filter(client_profile_id=request.POST.get('deed')).first()
    # Create a secure SSL context
    context = ssl.create_default_context()

    dates = numpy.empty(deed.duration, dtype=object)
    date_list = '\nДаты будущих платежей:'
    date_ = deed.date_signed
    for i in dates:
        date_ += relativedelta(months=+1)

        date_list += '\n' + datetime.strftime(date_, "%m/%d/%y")

    message = 'Данные о сделке\n' + 'Продукт - ' + deed.product.name + '\nСумма - ' + deed.loan_amount.__str__() + ' рублей\nРазмер платежа - ' + deed.regular_payment_size.__str__() + ' рублей\nПроцентная ставка - ' + deed.rate.__str__() + '%\nДлительность - ' + deed.duration.__str__() + ' месяцев' + date_list
    print(request.user.email)

    msg = 'From: {}\r\nTo: {}\r\nSubject: {}\n\n{}'.format(
        "test.artsiom@yandex.com", user_email,
        'Данные о сделке ' + deed.client_profile.name + ' ' + deed.client_profile.last_name, message
    )
    with smtplib.SMTP_SSL("smtp.yandex.com", port, context=context) as server:
        server.login("test.artsiom@yandex.com", password)
        server.sendmail("test.artsiom@yandex.com", user_email, msg.encode('utf8'))
    return render(request, 'dummy_tab.html')


def get_best_offer(request):
    form = Best_offer_form()
    if request.method == 'GET':
        return render(request, 'get_best_offer.html', {'form': form})
    else:
        products = Product.objects.filter(type=request.POST.get('desired_type'),
                                          max_amount__gte=request.POST.get('desired_amount'),
                                          min_amount__lte=request.POST.get('desired_amount'),
                                          max_duration__gte=request.POST.get('desired_duration'),
                                          min_duration__lte=request.POST.get('desired_duration'))
        rate_set = []
        final_set = []

        class Top3:
            def __init__(self, product_name, rate_top):
                self.product_name = product_name
                self.rate = rate_top

        for id_p, product in enumerate(products):
            rate = Interest_Rate.objects.filter(product=product,
                                                duration_more_than__lte=request.POST.get('desired_duration'),
                                                duration_less_than_or_equal__gte=request.POST.get(
                                                    'desired_duration')).first()

            print(rate)
            rate_set.append(rate)

        for i in range(0, 3):
            max1 = 1.0
            rate = None
            for j in range(len(rate_set)):
                if rate_set[j].rate < max1:
                    max1 = rate_set[j].rate
                    rate = Interest_Rate.objects.filter(product=rate_set[j].product, rate=rate_set[j].rate).first()
            rate_set.remove(rate)
            final_set.append(Top3(rate.product.name, (rate.rate*100).__str__() + '%'))


        print(final_set[0].product_name)
        return render(request, 'get_best_offer.html', {'form': form, 'result': final_set})
