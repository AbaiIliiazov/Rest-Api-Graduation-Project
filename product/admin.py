from django.contrib import admin
from product.models import Product, ProductImage

class ImageInlineAdmin(admin.TabularInline):
    model = ProductImage
    fields = ('image',)
    max_num = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]
    filter_list = ('created_by','created_at')


# Register your models here.
