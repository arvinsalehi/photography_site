from django.urls import path

from site_gallery.views import Gallery, photo_visit

app_name = "CategoryUrls"

urlpatterns = [
    path('category/<category_name>', Gallery.as_view(), name='category'),
    path('photo/<photo_id>', photo_visit, name='photo_visit')
]