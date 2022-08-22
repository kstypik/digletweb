# Generated by Django 4.1 on 2022-08-22 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("links", "0003_link_num_vote_down_link_num_vote_up_link_vote_score"),
    ]

    operations = [
        migrations.CreateModel(
            name="RelatedLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vote_score", models.IntegerField(db_index=True, default=0)),
                ("num_vote_up", models.PositiveIntegerField(db_index=True, default=0)),
                (
                    "num_vote_down",
                    models.PositiveIntegerField(db_index=True, default=0),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("url", models.URLField()),
                ("title", models.CharField(max_length=150)),
                (
                    "thumbnail",
                    models.ImageField(blank=True, upload_to="related_links_thumbnails"),
                ),
                ("domain", models.URLField()),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]