# Generated by Django 3.1.1 on 2020-11-08 09:40

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_repairs_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairs',
            name='last_name',
        ),
        migrations.AddField(
            model_name='repairs',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
