from django.shortcuts import render

from . import views

from django.urls import path, include
#Routes de l'application
urlpatterns = [
	path('', views.index, name='index'),
	path('question_du_jour', views.question_du_jour, name='question_du_jour')
]
