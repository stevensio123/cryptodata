from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('crypto/', views.crypto, name='Crypto_Home'),
    path('crypto/<str:indv_asset_id>/<str:indv_exchange_id>/',
         views.crypto, name='Crypto'),
]
