from django.db import models


class Site_Setting(models.Model):
    site_title = models.CharField(max_length=256)
    about_us = models.TextField()
    about_us_service = models.CharField(max_length=256)
    about_us_title = models.CharField(max_length=256)
    address = models.TextField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    tel_phone = models.CharField(max_length=8)
    CopyRight = models.TextField()

    def __str__(self):
        return self.site_title
