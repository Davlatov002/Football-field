
from django.urls import path
from . import views

urlpatterns = [

    path('create-foodballfield/', views.create_foodballfield, name='create-foodballfield'),
    path('update-foodballfield/<str:pk>/', views.update_foodballfield, name='update-foodballfield'),
    path('get-all-foodballfild/', views.get_all_foodballfild, name='get-all-foodballfild'),
    path('get-foodballfild-id/<str:pk>/', views.get_footballfild_id, name='get-all-foodballfild-id'),
    path('get-foodballfild-owner/', views.get_footballfild_owner, name='get-all-foodballfild-owner'),
    path('delete-foodballfield-id/<str:pk>/', views.delete_foodballfield, name='delete-foodballfield-id'),

    path('filter-stadium/', views.filter_stadium, name='filter-stadium'),

    path('get-all-bron/', views.get_all_brons, name='get-all-bron'),
    path('get-bron-id/<str:pk>/', views.get_footballfild_id, name='get-bron-id'),
    path('create-bron/', views.create_bron, name='create-bron'),
    path('update-bron-id/<str:pk>/', views.update_bron, name='update-bron-id'),
    path('bron-delete-id/<str:pk>/', views.bron_delete, name='bron-delete-id'),

]
