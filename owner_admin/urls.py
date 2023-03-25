from django.urls import path
from . import views

app_name = 'owner_admin'

urlpatterns = [
    path('', views.index, name='admin_home'),
    path('delete-testimonial/<int:testimonial_id>', views.delete_testimonial, name='delete_testimonial'),
    path('delete-offer/<int:offer_id>', views.delete_offer, name='delete_offer'),
    path('add-offer', views.add_or_edit_offer, name='add_offer'),
    path('edit-offer/<int:offer_id>', views.add_or_edit_offer, name='edit_offer'),
]
