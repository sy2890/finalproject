# Generated by Django 3.0 on 2019-12-08 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20191208_0232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='locatin',
            new_name='location',
        ),
    ]