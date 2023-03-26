from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from owner_admin.models import Offers


class OfferItem(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    number_of_people = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username}'s cart"
    
    def calculate_total_cost(self):
        total_cost = 0
        for cart_item in self.cartitem_set.all():
            total_cost += cart_item.offer.price * cart_item.number_of_people
        return total_cost
    
    def book(self, participantDict):
        # Calculate total cost
        total_cost = self.calculate_total_cost()
        
        # Create a new booking instance
        booking = Booking(user=self.user, total_cost=total_cost)
        booking.save()
        
        # Loop through all cart items and create booking items for each
        for cart_item in self.cartitem_set.all():
            booking_item = BookingItem(offer=cart_item.offer, number_of_people=cart_item.number_of_people, booking=booking)
            booking_item.save()
            booking_participants = participantDict[cart_item.id]
            # Loop through all booking participants and create a booking participant for each
            for participant in booking_participants:
                booking_participant = BookingParticipant(booking_item=booking_item, first_name=participant['first_name'], last_name=participant['last_name'], email=participant['email'], phone_number=participant['phone_number'])
                booking_participant.save()

        # Delete the cart after converting it to a booking
        self.delete()

class CartItem(OfferItem):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.offer.offer} offer for {self.number_of_people} in {self.cart}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"{self.user.username}'s booking for {self.date_created}"
    
class BookingItem(OfferItem):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.offer.offer} offer for {self.number_of_people} in {self.booking}"
    
class BookingParticipant(models.Model):
    booking_item = models.ForeignKey(BookingItem, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} for {self.booking_item}"