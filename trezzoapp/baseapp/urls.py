from django.urls import path
from baseapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service', views.service, name='service'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('ml', views.ml, name='ml'),
]