# Generated by Django 5.0.6 on 2024-07-23 12:29

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#FF0000', image_field=None, max_length=25, null=True, samples=None),
        ),
    ]
