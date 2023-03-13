from django.urls import path
from . import views 


urlpatterns = [
    path('', views.TestimonialListView.as_view(), name="list-testimonials"),
    path('add/', views.CreateTestimonialView.as_view(), name="add-testimonial"),
    # path('', views.upload, name='upload')
]

