from django.contrib import admin
from .models import Airport, Flight, Passenger, Booking, Meal


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'city', 'country')
    search_fields = ('code', 'name', 'city')


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'origin', 'destination', 'departure_time', 'price', 'available_seats', 'status')
    list_filter = ('status', 'origin', 'destination')
    search_fields = ('flight_number',)


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_reference', 'flight', 'passenger', 'booking_date', 'total_price', 'status', 'meal_name', 'short_description')
    list_filter = ('status', 'booking_date')
    search_fields = ('booking_reference', 'passenger__first_name', 'passenger__last_name')

    def meal_name(self, obj):
        return obj.meal.name if obj.meal else ''
    meal_name.short_description = 'Plat'

    def short_description(self, obj):
        return (obj.description[:50] + '...') if obj.description and len(obj.description) > 50 else (obj.description or '')
    short_description.short_description = 'Description'

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')
