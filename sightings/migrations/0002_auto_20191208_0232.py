# Generated by Django 3.0 on 2019-12-08 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='y',
            new_name='longitude',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='above_ground_sighter_measurement',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='color_notes',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='combination_of_primary_and_highlight_color',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='hectare',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='hectare_squirrel_number',
        ),
        migrations.RemoveField(
            model_name='squirrel',
            name='highlight_fur_color',
        ),
    ]
