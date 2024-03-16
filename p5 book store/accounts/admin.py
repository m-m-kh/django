from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('age',),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('age',),
        }),
    )
    list_display = UserAdmin.list_display + ('age',)
# admin.site.register(CustomUser, CustomUserAdmin)
