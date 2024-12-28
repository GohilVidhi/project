# Generated by Django 5.0.6 on 2024-07-30 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0017_delete_add_to_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addtocart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.products')),
                ('size_cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.size')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
    ]
