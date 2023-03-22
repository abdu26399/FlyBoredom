from django.contrib import admin
from django.db import models
from .models import Testimonial, Photos


class PhotosInLine(admin.TabularInline):
    model = Photos
    extra = 0


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    inlines = [PhotosInLine]


