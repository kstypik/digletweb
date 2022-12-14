# Generated by Django 4.1 on 2022-08-21 14:14

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=imagekit.models.fields.ProcessedImageField(
                blank=True, default="default_avatar.png", upload_to="avatars"
            ),
        ),
    ]
