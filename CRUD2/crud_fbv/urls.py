from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('view/<int:pk>', views.content_view, name='content_view'),
    path('new', views.content_create, name='content_new'),
    path('edit/<int:pk>', views.content_update, name='content_edit'),
    path('delete/<int:pk>', views.content_delete,name='content_delete'),
]