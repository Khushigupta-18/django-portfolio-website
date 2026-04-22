from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from contact import views as contact_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('contact/', contact_views.contact, name='contact'),
    path('admin/', include('dashboard.urls')),
    path('admin/projects/', include('portfolio.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
