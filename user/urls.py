from django.shortcuts import render

from . import views

from django.urls import path, include
urlpatterns = [
    path('', views.ConnectPageView.as_view()),
]
