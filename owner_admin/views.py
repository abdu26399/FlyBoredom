from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from testimonials.models import Testimonial
from owner_admin.models import Offers
from owner_admin.forms import AddOrEditOfferForm


redirect_url = '/'


@user_passes_test(lambda u: u.is_staff, login_url=redirect_url)
def index(request):
    latest_offers = Offers.objects.order_by('-date_added')
    latest_testimonials = Testimonial.objects.order_by('-date_added')
    return render(request, 'owner_admin/index.html', {'latest_testimonials': latest_testimonials,
                                                      'latest_offers': latest_offers})


@user_passes_test(lambda u: u.is_staff, login_url=redirect_url)
def delete_testimonial(request, testimonial_id):
    testimonial = Testimonial.objects.get(id=testimonial_id)
    testimonial.delete()
    return HttpResponseRedirect(reverse('owner_admin:admin_home'))


@user_passes_test(lambda u: u.is_staff, login_url=redirect_url)
def delete_offer(request, offer_id):
    offer = Offers.objects.get(id=offer_id)
    offer.delete()
    return HttpResponseRedirect(reverse('owner_admin:admin_home'))


@user_passes_test(lambda u: u.is_staff, login_url=redirect_url)
def add_or_edit_offer(request, offer_id=None):
    if offer_id:
        offer = Offers.objects.get(id=offer_id)
    else:
        offer = None
    if request.method == 'POST':
        form = AddOrEditOfferForm(request.POST, request.FILES, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('owner_admin:admin_home')
        else:
            message = 'Please correct the error below.'
            return render(request, 'owner_admin/add_or_edit_offer.html', {'form': form, 'message': message})
    else:
        form = AddOrEditOfferForm(instance=offer)
        return render(request, 'owner_admin/add_or_edit_offer.html', {'form': form})
