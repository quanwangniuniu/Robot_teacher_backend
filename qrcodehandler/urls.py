from django.urls import path
from qrcodehandler import views



urlpatterns = [
    path('generate_qrcode', views.generate_qrcode, name='generate_qrcode'),
]