from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect
from owner_admin.models import Offers
from django.views.generic import ListView
from django.views.generic.detail import DetailView

class HomeView(ListView):
    model = Offers
    context_object_name = 'latest_offers'
    template_name = 'offers/home.html'
    queryset = Offers.objects.all().order_by('-date_added')

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by location
        location_filter = self.request.GET.get('location')
        if location_filter:
            queryset = queryset.filter(location=location_filter)

        # Sort by price
        sort_by = self.request.GET.get('sort_by')
        sort_order = self.request.GET.get('sort_order')
        if sort_by == 'price':
            if sort_order == 'asc':
                queryset = queryset.order_by('price')
            elif sort_order == 'desc':
                queryset = queryset.order_by('-price')

        # Sort by date added
        elif sort_by == 'date_added':
            if sort_order == 'asc':
                queryset = queryset.order_by('date_added')
            elif sort_order == 'desc':
                queryset = queryset.order_by('-date_added')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add location filter options
        context['locations'] = set(offer.location for offer in Offers.objects.all())

        # Add current filter values to context
        context['current_location'] = self.request.GET.get('location')
        context['current_sort_by'] = self.request.GET.get('sort_by')
        context['current_sort_order'] = self.request.GET.get('sort_order')
        return context


class OfferDetailView(DetailView):
    model = Offers
    context_object_name = 'offer'
    template_name = 'offers/offer_detail.html'


class SearchView(ListView):
    model = Offers
    context_object_name = 'latest_offers'
    template_name = 'offers/search_results.html'
    queryset = Offers.objects.all().order_by('-date_added')

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by search term
        search_term = self.request.GET.get('search')
        if search_term:
            # Check if search term matches location
            queryset = queryset.filter(location__icontains=search_term)
            #
            # # Check if search term matches name
            # name_matches = queryset.filter(offer__icontains=search_term)
            # if len(name_matches) >= 3:
            #     queryset = name_matches

        return queryset


