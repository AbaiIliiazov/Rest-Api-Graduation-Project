from django.db import models
from my_user.models import User
from product.models import Product

class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, related_name='products_position', on_delete=models.CASCADE, default=None)
    order = models.ForeignKey('Order', related_name='positions', on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):

    NEW_STATUS ='NEW'
    IN_PROGRESS ='IN_PROGRESS'
    COMPLETE = 'COMPLETE'

    STATUS_CHOICES = ((NEW_STATUS, 'NEW'), (IN_PROGRESS, 'IN_PROGRESS'), (COMPLETE, 'COMPLETE'))

    creator = models.ForeignKey(User, verbose_name='buyer', on_delete=models.CASCADE,)
    products = models.ManyToManyField(Product, through=OrderedProduct, related_name="order")
    order_price = models.DecimalField(max_digits=10, decimal_places=2,)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW_STATUS)
    created_at = models.DateTimeField(verbose_name="created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated", auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return "order # %s made by %s with total amount of %s" % (self.id, self.creator, self.order_price)

