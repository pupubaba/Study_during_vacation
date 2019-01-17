from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContentList.as_view(), name='content_list'),
    path('view/<int:pk>', views.ContentView.as_view(), name='content_view'),
    path('new', views.ContentCreate.as_view(), name='content_new'),
    path('edit/<int:pk>', views.ContentUpdate.as_view(), name='content_edit'),
    path('delete/<int:pk>', views.ContentDelete.as_view(), name='content_delete'),
]