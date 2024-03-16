from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'age')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )



