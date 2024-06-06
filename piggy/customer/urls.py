from django.contrib import admin
from django.urls import path 
from django.conf.urls.static import static 
from django.conf import settings
from .views import *

urlpatterns = [
    path('customer_registration',customer_registration,name='customer_registration'),
    path('user_login',user_login,name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)