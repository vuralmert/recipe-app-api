# Generated by Django 3.2.14 on 2022-08-04 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='time_minutes',
        ),
    ]
