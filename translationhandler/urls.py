'''
 translationhandler/urls
'''
from django.urls import path
from translationhandler import views

urlpatterns = [
    path('text_translation', views.text_translation, name='text_translation'),
]