from rest_framework.serializers import ModelSerializer

from digletweb.users.models import User


class UserAvatarSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["avatar"]

    def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)


class UserBackgroundSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["background_image"]

    def save(self, *args, **kwargs):
        if self.instance.background_image:
            self.instance.background_image.delete()
        return super().save(*args, **kwargs)
