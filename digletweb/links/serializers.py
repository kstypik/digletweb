from rest_framework import serializers

from digletweb.links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "title", "slug", "domain", "description", "thumbnail", "author"]
        read_only_fields = ["author"]
