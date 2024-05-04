from django.urls import path

from . import views

urlpatterns = [

    path('', views.homepage, name=""),

    path('register', views.register, name="register"),

    path('user-login', views.user_login, name="user-login"),

    path('dashboard', views.dashboard, name="dashboard"),
    
    path('product-details', views.product_details, name="product-details"),

    path('logout', views.logout, name="logout")
]








