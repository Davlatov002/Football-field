from django.urls import path
from . import views

urlpatterns = [

    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get-user/', views.get_user, name='get-user'),
    path('get-user-all/', views.get_all_user, name='get-user-all'),
    path('create-user/', views.create_user, name='create-user'),
    path('update-user/', views.update_user, name='update-user'),
    path('delete-user/', views.delete_user, name='delete-user'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair')

]


