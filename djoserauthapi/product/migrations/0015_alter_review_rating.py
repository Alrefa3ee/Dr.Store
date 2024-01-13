# Generated by Django 5.0.1 on 2024-01-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, null=True),
        ),
    ]