from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('cards/', views.cards_index, name='cards_index'),
    # path('cards/<int:card_id>/', views.cards_detail, name='cards_detail'),
    path('cards/', views.CardList.as_view(), name='card_index'),
    path('cards/<int:card_id>/', views.CardDetail.as_view(), name='card_detail'),
    path('cards/create/', views.CardCreate.as_view(), name='card_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='card_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='card_delete'),
    path('cards/<int:card_id>/add_cleaning/',
         views.add_cleaning, name='add_cleaning'),
    path('vendors/', views.VendorList.as_view(), name='vendor_index'),
    path('vendors/<int:vendor_id>/',
         views.VendorDetail.as_view(), name='vendor_detail'),
    path('vendors/create/', views.VendorCreate.as_view(), name='vendor_create'),
    path('vendors/<int:pk>/update/',
         views.VendorUpdate.as_view(), name='vendor_update'),
    path('vendors/<int:pk>/delete/',
         views.VendorDelete.as_view(), name='vendor_delete'),
]
