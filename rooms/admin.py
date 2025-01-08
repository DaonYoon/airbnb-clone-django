from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ("name", "price", "kind", "owner")
    list_filter=("country", "city", "price", "amenties")


@admin.register(Amenity)
class Amenitydmin(admin.ModelAdmin):
    
    list_display=("name", "description", "created_at", "updated_at")
    
