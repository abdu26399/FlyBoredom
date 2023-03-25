from django.http import JsonResponse
from .models import BackgroundImage
from owner_admin.models import Offers
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView


class HomeView(ListView):
    model = Offers
    context_object_name = 'latest_offers'
    template_name = 'offers/home.html'
    queryset = Offers.objects.all().order_by('-date_added')


class OfferDetailView(DetailView):
    model = Offers
    context_object_name = 'offer'
    template_name = 'offers/offer_detail.html'
