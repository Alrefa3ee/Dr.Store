# Generated by Django 5.0.1 on 2024-01-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_category_slug_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]