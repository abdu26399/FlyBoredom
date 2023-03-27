from django.db import models
from django.utils import timezone

from uuid import uuid4


class Offers(models.Model):
    offer = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    spots_available = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.image:
            ext = self.image.name.split('.')[-1]
            self.image.name = f'{uuid4()}.{ext}'
        super().save(*args, **kwargs)

    def status(self):
        if self.spots_available == 0:
            return 'Sold Out'
        elif self.date > timezone.now():
            return 'Upcoming'
        elif self.date < timezone.now():
            return 'Expired'

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Offers'

    def __str__(self):
        return self.offer
