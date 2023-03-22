from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from testimonials.models import Testimonial, Photos


def index(request):
    latest_testimonials = Testimonial.objects.order_by('-date_added')
    return render(request, 'owner_admin/index.html', {'latest_testimonials': latest_testimonials})


def delete_testimonial(request, testimonial_id):
    testimonial = Testimonial.objects.get(id=testimonial_id)
    testimonial.delete()
    return HttpResponseRedirect(reverse('owner_admin:admin_home'))
