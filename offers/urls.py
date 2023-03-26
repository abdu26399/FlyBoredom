from django.urls import path
from .views import HomeView, OfferDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('offer/<int:pk>/', OfferDetailView.as_view(), name='offer_detail'),
    # path('offer_search/', OfferSearchView.as_view(), name='offer_search'),
]