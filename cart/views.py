import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import requests
from .models import Cart, CartItem
from owner_admin.models import Offers


redirect_url = 'testimonials:list-testimonials'


@user_passes_test(lambda u: u.is_authenticated, login_url=redirect_url)
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart(user=request.user)
        cart.save()
    cart_items = cart.cartitem_set.all()
    total_cost = cart.calculate_total_cost()
    context = {'cart_items': cart_items, 'total_cost': total_cost}
    return render(request, 'cart/view_cart.html', context)


@user_passes_test(lambda u: u.is_authenticated, login_url=redirect_url)
def add_to_cart(request, offer_id):
    offer = Offers.objects.get(id=offer_id)
    number_of_people = int(request.POST.get('quantity', 1))
    if number_of_people <= 0:
        messages.error(request, 'Invalid quantity.')
        return redirect('view_cart')
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart(user=request.user)
        cart.save()
    cart_item, created = CartItem.objects.get_or_create(cart=cart, offer=offer)
    if not created:
        cart_item.number_of_people += number_of_people
        cart_item.save()
    else:
        cart_item.number_of_people = number_of_people
        cart_item.save()
    messages.success(request, f"{offer.offer} offer added to cart.")
    return redirect('view_cart')


@user_passes_test(lambda u: u.is_authenticated, login_url=redirect_url)
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    messages.success(request, f"{cart_item.offer.offer} offer removed from cart.")
    return redirect('view_cart')


@user_passes_test(lambda u: u.is_authenticated, login_url=redirect_url)
def checkout(request):
    try:
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            messages.warning(request, "Your cart is empty.")
            return redirect('view_cart')
        
        # Get the conversion rates from the API
        response = requests.get('https://api.exchangerate-api.com/v4/latest/CAD')
        if not response.ok:
            messages.error(request, "Unable to get the conversion rates.")
            return redirect('view_cart')
        conversion_rates = json.dumps(response.json()["rates"])
        
        if request.method == 'POST':
            participantDict = {}
            for item in cart.cartitem_set.all():
                participants = []
                for i in range(item.number_of_people):
                    first_name = request.POST.get(f"first_name_{item.id}_{i+1}")
                    last_name = request.POST.get(f"last_name_{item.id}_{i+1}")
                    email = request.POST.get(f"email_{item.id}_{i+1}")
                    phone = request.POST.get(f"phone_{item.id}_{i+1}")
                    try:
                        validate_email(email)
                        newObj = {"first_name":first_name, "last_name":last_name, "email":email, "phone_number":phone}
                        participants.append(newObj)
                    except ValidationError:
                        messages.error(request, f"{email} is not a valid email address. Try again")
                        return redirect('view_cart')
                participantDict[item.id] = participants
                cart.book(participantDict)
                messages.success(request, "Booking successful! Thank you.")
                return redirect('view_cart')
            
        context = {'total_cost': cart.calculate_total_cost(), 'cart_items': cart.cartitem_set.all(), 'conversion_rates': conversion_rates}
        return render(request, 'cart/checkout.html', context)
    
    except Exception as e:
        messages.error(request, str(e))
        return redirect('view_cart')
