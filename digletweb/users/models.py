from django.contrib.auth.models import AbstractUser
from django.db import models

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

from digletweb.users.validators import background_image_restriction


def user_directory_path(instance, filename):
    return f"{instance.username}_{filename}"


def profile_background_directory_path(instance, filename):
    return f"profile_backgrounds/{instance.username}_{filename}"


class User(AbstractUser):
    avatar = ProcessedImageField(
        upload_to=user_directory_path,
        blank=True,
        default="default_avatar.png",
        processors=[ResizeToFill(150, 150)],
        format="JPEG",
        options={"quality": 60},
    )
    avatar_small = ImageSpecField(
        source="avatar", processors=[ResizeToFill(40, 40)], format="JPEG"
    )
    avatar_extra_small = ImageSpecField(
        source="avatar", processors=[ResizeToFill(30, 30)], format="JPEG"
    )

    background_image = models.ImageField(
        validators=[background_image_restriction],
        upload_to=profile_background_directory_path,
        blank=True,
    )
