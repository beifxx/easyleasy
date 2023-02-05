from django.urls import path
from . import views

urlpatterns = [
    path('u/home/', views.user_home_page),
    path('u/product/<int:product_id>', views.product_page),
    path('u/support/', views.support_page),
    path('u/news/', views.news_page),
    path('u/products', views.products_page),
    path('u/account', views.my_user_account),
    path('u/jur/new_request', views.jur_new_request),
    path('u/new_request/type', views.new_request_choose_type),
    path('u/phys/new_request', views.phys_new_request),
    path('a/phys/download', views.download_phys_zip),
    path('a/jur/download', views.download_jur_zip),
    path('download_contract', views.download_contract),
    path('a/support_requests', views.support_requests_page),
    path('a/deeds', views.deeds_page),
    path('a/deed/<int:deed_id>', views.admin_single_deed),
    path('a/stats', views.admin_stats),
    path('get_mail', views.get_mail),
    path('u/get_best', views.get_best_offer),


    path('a/home', views.admin_home_page),
    path('logout', views.logout),
    path('a/applications', views.admin_applications_page),
    path('a/application/<int:application_id>', views.admin_single_application),





    path('', views.login_page),
    path('register', views.register_page),
]