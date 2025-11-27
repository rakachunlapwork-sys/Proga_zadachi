from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all_character/', views.get_all_character, name='all_character'),
    path('character/<int:id>', views.get_character, name='character'),
]
