# Generated by Django 5.0.6 on 2024-08-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0023_add_whishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=60, null=True)),
                ('discount', models.IntegerField()),
                ('expiry_date', models.DateTimeField()),
            ],
        ),
    ]
