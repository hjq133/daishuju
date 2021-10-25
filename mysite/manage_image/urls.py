from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_image/', views.create_image, name='login'),
    path('get_image_list/', views.get_image_list, name='register'),
    path('delete_image/', views.delete_image, name='get_user')
]