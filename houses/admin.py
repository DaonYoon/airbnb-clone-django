from django.contrib import admin
from .models import House

# Register your models here.


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    fields = ("name", "address", ("price", "pets_allowed"))
    list_display = ("name", "price", "address", "pets_allowed")
    list_filter = ("pets_allowed", "price")
    search_fields = ("address",)

    list_display_links = ("name", "price")
