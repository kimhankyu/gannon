from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('gameinfo/<int:game_id>', views.gameinfoView, name='gameinfo'),

]
