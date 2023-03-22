from django.db import models


class Offers(models.Model):
    offer = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Offers'

    def __str__(self):
        return self.offer
