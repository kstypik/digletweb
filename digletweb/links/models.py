from autoslug import AutoSlugField
from digletweb.users.models import User
from django.db import models
from model_utils.models import TimeStampedModel


def thumbnail_path(instance, filename):
    try:
        file_ext = filename.split(".")[-1]
    except KeyError:
        file_ext = ""
    return f"{instance.slug}.{file_ext}"


class Link(TimeStampedModel):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="title", unique=True)
    domain = models.URLField()
    description = models.TextField(max_length=1000)
    thumbnail = models.ImageField(upload_to=thumbnail_path, blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
