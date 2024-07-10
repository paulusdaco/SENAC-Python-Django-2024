from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event_list/', views.event_list, name='event_list'),
    path('event_create/', views.event_create, name='event_create'),
    path('event_detail/<int:pk>/', views.event_detail, name='event_detail'),
    path('event_edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('event_delete/<int:pk>/', views.event_delete, name='event_delete'),
]


