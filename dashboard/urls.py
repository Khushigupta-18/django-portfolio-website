from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('messages/', views.message_list, name='dashboard_messages'),
    path('messages/delete/<int:pk>/', views.message_delete, name='message_delete'),
]
