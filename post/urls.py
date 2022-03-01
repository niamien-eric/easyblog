from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.postAll, name='home'),
    path('post/<slug:slug>/', views.postDetails,name='details'),
    path('add/', views.postAdd,name='add_post'),
    path('update/<slug:slug>/', views.postUpdate,name='update'),
    path('delete/<slug:slug>/', views.postDelete,name='delete'),
]
