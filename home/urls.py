from django import urls
from django.contrib import admin
from django.contrib.admin.sites import site
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("signup", views.handelSignup, name='handelSignup'),
    path("login", views.handelLogin, name='handelLogin'),
    path("logout", views.handelLogout, name='handelLogout'),
]