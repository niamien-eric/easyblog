from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    path('signup/', views.sign_up, name='signup'),
    path('signout/', views.sign_out, name='signout'),
]
