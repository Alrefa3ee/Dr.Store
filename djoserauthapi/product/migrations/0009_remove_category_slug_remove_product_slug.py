# Generated by Django 5.0.1 on 2024-01-13 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_order_products_remove_product_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]