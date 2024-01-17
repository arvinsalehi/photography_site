from django.db import models

from photography_site.utilities import file_upload_name
# from django.db.models.signals import pre_save, post_save
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    visit = models.IntegerField(default=0, null=True)
    image = models.ImageField(upload_to=file_upload_name, null=True, blank=False)

    def save(self, *args, **kwargs):
        super(Category, self).save()
        img = Image.open(self.image.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (900, 874)
            img.thumbnail(new_img)
            img.save(self.image.path)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# def pre_save_image_resize(sender, instance, *args, **kwargs):
#     instance.image = get_thumbnail(instance.image, '500x600', quality=99, format='JPEG')
#
#
# pre_save.connect(pre_save_image_resize, sender=Category)
