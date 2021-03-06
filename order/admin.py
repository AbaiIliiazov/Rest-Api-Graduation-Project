from django.contrib import admin
from order.models import Order, OrderedProduct

class OrderedProductInLine(admin.TabularInline):
    model = OrderedProduct
    raw_id_fields = ['order']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','creator','order_price','status','created_at', 'updated_at']
    list_filter = ['creator', 'created_at','updated_at']
    inlines = [OrderedProductInLine]


