from django.db import models
from product.models import Product
from my_user.models import User

class Review(models.Model):
    CHOICES_LIST = ((1, '1',), (2, '2',), (3, '3',), (4, '4',), (5, '5',))

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    product = models.ForeignKey(Product, verbose_name='Product', related_name='reviews', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE,)
    text = models.TextField(max_length=1000, verbose_name='review text')
    rating = models.PositiveIntegerField(verbose_name='Rating', choices=CHOICES_LIST)
    created_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return "Rating by %s for %s " % (self.creator, self.product)

