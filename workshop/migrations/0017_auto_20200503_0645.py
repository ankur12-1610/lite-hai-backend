# Generated by Django 2.2.6 on 2020-05-03 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0016_auto_20200503_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tag_name',
        ),
    ]