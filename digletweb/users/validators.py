from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

MIN_WIDTH = settings.PROFILE_BACKGROUND_IMAGE_MIN_WIDTH
MIN_HEIGHT = settings.PROFILE_BACKGROUND_IMAGE_MIN_HEIGHT


def background_image_restriction(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width < MIN_WIDTH or image_height < MIN_HEIGHT:
        raise ValidationError(
            f"Background image does not meet the dimension criteria ({MIN_WIDTH}x{MIN_HEIGHT})."
        )
