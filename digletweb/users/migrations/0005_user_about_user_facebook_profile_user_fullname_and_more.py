# Generated by Django 4.1 on 2022-08-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_background_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="about",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="facebook_profile",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="fullname",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("U", "Unspecified"), ("F", "Female"), ("M", "Male")],
                default="U",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="instagram_profile",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="user",
            name="twitter_profile",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="user",
            name="website",
            field=models.URLField(blank=True),
        ),
    ]
