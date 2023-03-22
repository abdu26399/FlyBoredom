from django.contrib import admin
from owner_admin.models import Offers


class OffersAdmin(admin.ModelAdmin):
    list_display = ('offer', 'description', 'date_added', 'from_date', 'to_date', 'image', 'price')


admin.site.register(Offers)
