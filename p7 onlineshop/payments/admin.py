from django.contrib import admin
from .models import TransactionModel
# Register your models here.

class TransactionInline(admin.StackedInline ):
    model = TransactionModel

    readonly_fields = ('id','link','status','track_id')
    extra = 0




@admin.register(TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'status')
