from django.contrib import admin

from site_photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'id']


admin.site.register(Photo, PhotoAdmin)
