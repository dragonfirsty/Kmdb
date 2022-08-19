from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email","first_name","last_name","birthdate","bio")}),
        ("Permissions", {"fields": ("is_superuser","is_staff","is_active","is_critic")}),
        ("Important dates", {"fields": ("last_login","date_joined")}),
    )


admin.site.register(User, CustomUserAdmin)

