from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from vote.models import VoteModel

from digletweb.users.models import User


def thumbnail_path(instance, filename):
    try:
        file_ext = filename.split(".")[-1]
    except KeyError:
        file_ext = ""
    return f"{instance.slug}.{file_ext}"


class Link(VoteModel, TimeStampedModel):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="title", unique=True)
    domain = models.URLField()
    description = models.TextField(max_length=1000)
    thumbnail = models.ImageField(upload_to=thumbnail_path, blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class RelatedLink(VoteModel, TimeStampedModel):
    url = models.URLField()
    parent = models.ForeignKey(Link, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField(upload_to="related_links_thumbnails", blank=True)
    domain = models.URLField(blank=True)


class Comment(TimeStampedModel):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    message = models.TextField()
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, related_name="replies"
    )
