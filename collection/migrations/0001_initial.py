# Generated by Django 3.1.7 on 2021-03-15 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0007_auto_20210312_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100, verbose_name='Header')),
                ('text', models.TextField(max_length=1000, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'compilation',
                'verbose_name_plural': 'compilations',
            },
        ),
        migrations.CreateModel(
            name='ProductInCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='collection.collection')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(related_name='collections', through='collection.ProductInCollection', to='product.Product'),
        ),
    ]
