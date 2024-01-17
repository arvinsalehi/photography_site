from django.urls import path

from site_service.views import services_page

app_name = 'Services'

urlpatterns = [
    path('services', services_page, name='services')
]
