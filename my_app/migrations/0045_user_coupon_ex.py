# Generated by Django 5.0.6 on 2024-12-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0044_remove_addtocart_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_coupon',
            name='ex',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
