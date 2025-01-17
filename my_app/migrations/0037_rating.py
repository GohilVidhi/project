# Generated by Django 5.0.6 on 2024-09-04 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0036_order_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.products')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
    ]
