# Generated by Django 4.0.4 on 2022-05-05 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotels',
            old_name='eminities',
            new_name='emenities',
        ),
    ]
