# Generated by Django 5.0.6 on 2024-07-30 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0014_products_color1'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]