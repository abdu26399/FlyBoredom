from django.db import models
from django.conf import settings


class Testimonial(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    testimonial = models.TextField()
    photo = models.ImageField(upload_to='photos',null=True,blank=True)   
    date_added = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-date_added']        

    def __str__(self):
        return self.title    


class Photos(models.Model):
    testimonial = models.ForeignKey(Testimonial, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/',null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']        

    