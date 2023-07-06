from django.contrib import admin
from django.urls import path, include
import coinapi_app.views

urlpatterns = [
    path('', include('coinapi_app.urls')),
]
