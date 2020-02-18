from django.urls import path
from baseapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ml', views.ml, name='ml'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]