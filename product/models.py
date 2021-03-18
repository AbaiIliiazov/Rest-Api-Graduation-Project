from django.db import models

class Product(models.Model):

    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10,decimal_places=2,default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images', blank=True)
