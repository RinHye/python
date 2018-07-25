from django.shortcuts import render
from django.contrib.auth.views import login, logout
from . import views

from django.urls import path, include
from django.conf.urls import url
#Routes de l'application
urlpatterns = [
	url(r'^$', login, {'template_name': 'accounts/login.html'}, name='index'),
    path(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout' ),
	path('', views.index, name='index'),
	path('matches', views.matches, name='matches'),
	path('question_du_jour', views.question_du_jour, name='question_du_jour')
]
