# Generated by Django 5.0.6 on 2024-07-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_products_color_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]