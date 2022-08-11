# Generated by Django 4.1 on 2022-08-11 15:10

from django.db import migrations

import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="title", unique=True
            ),
        ),
    ]