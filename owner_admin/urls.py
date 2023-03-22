from django.urls import path
from . import views

app_name = 'owner_admin'

urlpatterns = [
    path('', views.index, name='admin_home'),
    path('delete_testimonial/<int:testimonial_id>', views.delete_testimonial, name='delete_testimonial'),
]