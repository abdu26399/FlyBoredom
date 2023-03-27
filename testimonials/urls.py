from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views 

app_name = 'testimonials'

urlpatterns = [
    path('', views.TestimonialListView.as_view(), name="list-testimonials"),
    path('add/', login_required(views.CreateTestimonialView.as_view()), name="add-testimonial"),
]

