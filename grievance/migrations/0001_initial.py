# Generated by Django 2.2.13 on 2021-12-08 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, null=True)),
                ('branch', models.CharField(choices=[('Architecture', 'Architecture'), ('Ceramic', 'Ceramic'), ('Chemical', 'Chemical'), ('Civil', 'Civil'), ('Computer Science', 'Computer Science'), ('Electrical', 'Electrical'), ('Electronics', 'Electronics'), ('Mechanical', 'Mechanical'), ('Metallurgical', 'Metallurgical'), ('Mining', 'Mining'), ('Pharmaceutical', 'Pharmaceutical')], max_length=200, null=True)),
                ('course', models.CharField(choices=[('B.Tech', 'B.Tech'), ('IDD', 'IDD'), ('M.Tech', 'M.Tech')], max_length=200, null=True)),
                ('year', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')], max_length=200, null=True)),
                ('type_of_complaint', models.CharField(choices=[('Security', 'Security'), ('Health&Hygiene', 'Health&Hygiene'), ('HostelMess', 'HostelMess'), ('Academics', 'Academics'), ('Council', 'Council'), ('Others', 'Others')], max_length=200, null=True)),
                ('description', models.TextField(max_length=4000, null=True)),
                ('drive_link', models.URLField(blank=True, max_length=400)),
                ('time', models.DateField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Closed'), (2, 'Registered'), (3, 'Pending')], default=3)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
