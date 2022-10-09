from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from leasingapp.forms import Login_form


def index(request):
    form = Login_form
    return render(request, "login_page.html", {"form": form})