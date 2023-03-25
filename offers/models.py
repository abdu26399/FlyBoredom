from django.db import models


class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='background_images/')
