# Generated by Django 2.2.10 on 2020-11-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0026_workshop_is_workshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entity',
            name='is_permanent',
            field=models.BooleanField(default=False),
        ),
    ]
