# Generated by Django 3.1.3 on 2021-03-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]
