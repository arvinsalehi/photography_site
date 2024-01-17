from django.contrib import admin

from site_category.models import Category
from site_photo.models import Photo


class PhotoTabular(admin.TabularInline):
    model = Photo.categories.through


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__']
    inlines = [
        PhotoTabular,
    ]


admin.site.register(Category, CategoryAdmin)
