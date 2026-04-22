from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='dashboard_projects'),
    path('add/', views.project_add, name='project_add'),
    path('edit/<int:pk>/', views.project_edit, name='project_edit'),
    path('delete/<int:pk>/', views.project_delete, name='project_delete'),
    path('skills/', views.skill_list, name='dashboard_skills'),
    path('skills/add/', views.skill_add, name='skill_add'),
    path('skills/edit/<int:pk>/', views.skill_edit, name='skill_edit'),
    path('skills/delete/<int:pk>/', views.skill_delete, name='skill_delete'),
    path('services/', views.service_list, name='dashboard_services'),
    path('services/add/', views.service_add, name='service_add'),
    path('services/edit/<int:pk>/', views.service_edit, name='service_edit'),
    path('services/delete/<int:pk>/', views.service_delete, name='service_delete'),
]
