from django.contrib import admin

from order.models import Order, OrderItem
from payments.admin import TransactionInline
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['price']
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'datetime_created', 'is_paid')
    inlines = [OrderItemInline,
               TransactionInline]

