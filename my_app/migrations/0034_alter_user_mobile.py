# Generated by Django 5.0.6 on 2024-08-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0033_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]