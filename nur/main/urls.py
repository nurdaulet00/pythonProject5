from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about, name='about'),
    path('end', views.end, name='contacts'),
    path('index', views.index, name='home'),
    path('page', views.page, name='page'),
    path('layout', views.layout, name='pro'),

]
