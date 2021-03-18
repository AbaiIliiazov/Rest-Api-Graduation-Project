from django.db import models
from product.models import Product


class ProductInCollection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    collection = models.ForeignKey('Collection', related_name='collections', on_delete=models.CASCADE, default=None)


class Collection(models.Model):

    class Meta:
        verbose_name = 'compilation'
        verbose_name_plural = 'compilations'

    title = models.TextField(max_length=100, verbose_name='Header')
    text = models.TextField(max_length=1000, verbose_name='Text')
    products = models.ManyToManyField(Product, through=ProductInCollection, related_name='collections')
    created_at = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated',
        auto_now=True
    )

    def __str__(self):
        return self.title











# Create your models here.
