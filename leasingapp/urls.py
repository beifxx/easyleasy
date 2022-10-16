from django.urls import path
from . import views

urlpatterns = [
    #path('u/home/', views.home_page),
    path('', views.login_page),
    path('register', views.register_page),
]