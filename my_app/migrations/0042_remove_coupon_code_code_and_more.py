# Generated by Django 5.0.6 on 2024-12-27 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0041_coupon_code_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon_code',
            name='code',
        ),
        migrations.RemoveField(
            model_name='coupon_code',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='coupon_code',
            name='one_time_use',
        ),
        migrations.RemoveField(
            model_name='coupon_code',
            name='user_id',
        ),
        migrations.AddField(
            model_name='coupon_code',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='User_coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_id', models.ForeignKey(blank=True, max_length=60, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.coupon_code')),
                ('user_id', models.ForeignKey(blank=True, max_length=60, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
        ),
    ]
