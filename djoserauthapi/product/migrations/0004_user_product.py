# Generated by Django 5.0.1 on 2024-01-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='product',
            field=models.ManyToManyField(blank=True, to='product.product'),
        ),
    ]
