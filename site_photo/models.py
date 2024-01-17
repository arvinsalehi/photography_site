from django.db import models

from photography_site.utilities import file_upload_name
from site_category.models import Category


class PhotoManager(models.Manager):

    def get_by_id(self, photo_id):
        qs = self.get_queryset().filter(id=photo_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)


class Photo(models.Model):
    title = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category, blank=False)
    description = models.TextField(max_length=30, blank=True, null=True, default='')
    image = models.ImageField(upload_to=file_upload_name)
    # visit = models.IntegerField(default=0)

    objects = PhotoManager()

    def __str__(self):
        return self.title
