from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'nickname')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'age', 'nickname')}),
    )