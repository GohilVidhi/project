# Generated by Django 5.0.6 on 2024-08-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0035_alter_user_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='add_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]