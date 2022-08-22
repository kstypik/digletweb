from rest_framework import serializers

from digletweb.users.models import User


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["avatar"]

    def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)


class UserBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["background_image"]

    def save(self, *args, **kwargs):
        if self.instance.background_image:
            self.instance.background_image.delete()
        return super().save(*args, **kwargs)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "full_name",
            "gender",
            "location",
            "website",
            "facebook_profile",
            "twitter_profile",
            "instagram_profile",
            "about",
            "avatar",
            "background_image",
        ]
