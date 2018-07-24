from django.shortcuts import render

from . import views

from django.urls import path, include
#Routes de l'application
urlpatterns = [
	path('', views.index, name='index'),
    path('<int:id>', views.question, name="affiche_question"),
    path('form', views.question_form, name="form_question"),
    #path('contact/', views.contact, name="contact"),
]
