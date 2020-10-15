from django.contrib import admin
from django.urls import path
from .views import Login, logout_request, GmailScrapingAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login', Login.as_view()),
    path('logout', logout_request),
    path('gmail-scraping', GmailScrapingAPIView.as_view()),



]