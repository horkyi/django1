from django.urls import path
from main import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus', views.about, name='about'),
    path('admin', admin.site.urls)
]
