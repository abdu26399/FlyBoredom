from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Testimonial, Photos

from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.urls import reverse

class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'testimonials/list_testimonials.html'

#LoginRequiredMixin
class CreateTestimonialView(CreateView):
    'View to create testimonials'
    model = Testimonial
    template_name = 'testimonials/testimonial_form.html'
    fields = '__all__'


    def form_valid(self, form):
        instance = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            Photos.objects.create(testimonial=instance, photo=image)

        return super(CreateTestimonialView, self).form_valid(form)
        

    def get_success_url(self):
        return reverse('list-testimonials')