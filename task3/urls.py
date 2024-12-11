from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('game/', views.game, name='game'),
    path('platform/', views.platform, name='platform'),
]