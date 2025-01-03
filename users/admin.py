from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #   fieldsets = None
    #  fields = ("email", "password", "name")
    fieldsets = (
        ("Profile", {"fields": ("username", "password", "name", "email", "is_host")}),
    )
    
    list_display = ("username", "email", "name", "is_host")
