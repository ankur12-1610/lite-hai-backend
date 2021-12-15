# Generated by Django 2.2.13 on 2021-12-12 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentication", "0012_auto_20200303_2140"),
    ]

    operations = [
        migrations.CreateModel(
            name="NoticeBoard",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("date", models.DateTimeField()),
                ("notice_url", models.URLField(blank=True, null=True)),
                ("upvote", models.IntegerField(default=0)),
                ("downvote", models.IntegerField(default=0)),
                (
                    "notice_contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="notice_contact",
                        to="authentication.UserProfile",
                    ),
                ),
            ],
        ),
    ]
