from django.contrib import admin
from django.urls import path
from app_crud import views

# rota, view, nome de referencia

    # site.com
    # path('')

    # site.com/rota
    # path('rota/', view a ser renderizada, nome de referencia para realizar tratamentos)

urlpatterns = [
    path('', views.Home, name='home' ),
    path('users/', views.Users, name="users-list")
]
