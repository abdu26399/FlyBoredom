from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Testimonial

from django.views.generic.list import ListView

#LoginRequiredMixin
class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'testimonials/list_testimonials.html'
