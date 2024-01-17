"""photography_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from photography_site import settings
from photography_site.views import home_page, about_page

urlpatterns = [
    path('', home_page, name="Home"),
    path('', include('site_gallery.urls', namespace='CategoryUrls')),
    path('', include('site_contact.urls', namespace='Contact_Us')),
    path('', include('site_service.urls', namespace='Services')),
    path('about-us', about_page, name="About-us"),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # add root static files!
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)