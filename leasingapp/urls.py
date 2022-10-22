from django.urls import path
from . import views

urlpatterns = [
    path('u/home/', views.home_page),
    path('u/product/<int:product_id>', views.product_page),
    path('u/support/', views.support_page),
    path('', views.login_page),
    path('register', views.register_page),
]