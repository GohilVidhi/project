# Generated by Django 5.0.6 on 2024-08-08 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0028_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='address1',
        ),
    ]
