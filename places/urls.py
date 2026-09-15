from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.place_list, name='place_list'),
    path('places/<str:place_id>/', views.place_detail, name='place_detail'),
    path('add/', views.add_place, name='add_place'),
]