from django.contrib import admin
from cart.models import Cart, Booking, CartItem, BookingItem, BookingParticipant


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    fields=["offer", "number_of_people"]
    can_delete = False


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_created', 'date_modified', 'item_count']
    readonly_fields = ['item_count']
    inlines=[CartItemAdmin]

    def item_count(self, obj):
        return obj.cartitem_set.count()
    item_count.short_description = 'Number of items'

class BookingParticipantInline(admin.TabularInline):
    model = BookingParticipant


class BookingItemInline(admin.TabularInline):
    model = BookingItem
    fields=('offer', 'number_of_people')
    show_change_link = True
    


class BookingItemAdmin(admin.ModelAdmin):
    model = BookingItem
    inlines = [BookingParticipantInline,]
    can_delete = False


class BookingAdmin(admin.ModelAdmin):
    inlines = [BookingItemInline,]


admin.site.register(Cart, CartAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingItem, BookingItemAdmin)