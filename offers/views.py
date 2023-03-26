from django.http import JsonResponse
from django.views.generic.edit import FormMixin, FormView

# from .forms import OfferSearchForm
# from .models import BackgroundImage
from owner_admin.models import Offers
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.db.models import Q


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

        # Filter by price
        price_filter = self.request.GET.get('price')
        if price_filter:
            if price_filter == 'asc':
                queryset = queryset.order_by('price')
            elif price_filter == 'dsc':
                queryset = queryset.order_by('-price')

        # Filter by date added
        date_filter = self.request.GET.get('date_added')
        if date_filter:
            if date_filter == 'asc':
                queryset = queryset.order_by('date_added')
            elif date_filter == 'dsc':
                queryset = queryset.order_by('-date_added')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add location filter options
        context['locations'] = set(offer.location for offer in context['latest_offers'])

        # Add current filter values to context
        context['current_location'] = self.request.GET.get('location')
        context['current_price'] = self.request.GET.get('price')
        context['current_date_added'] = self.request.GET.get('date_added')
        return context



class OfferDetailView(DetailView):
    model = Offers
    context_object_name = 'offer'
    template_name = 'offers/offer_detail.html'


# class OfferSearchView(FormView):
#     template_name = 'offers/search_results.html'
#     form_class = OfferSearchForm
#
#     def form_valid(self, form):
#         search_query = form.cleaned_data.get('search_query')
#         results = Offers.objects.filter(Q(offer__icontains=search_query) | Q(location__icontains=search_query))
#         context = {'results': results}
#         return self.render_to_response(context)
#
#     def form_invalid(self, form):
#         return JsonResponse({'error': 'Invalid form submission.'})
