from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='cards_index'),
    path('cards/<int:card_id>/', views.cards_detail, name='cards_detail')
]
