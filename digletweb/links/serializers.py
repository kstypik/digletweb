from digletweb.links.models import Link
from rest_framework import serializers


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "title", "slug", "domain", "description", "thumbnail", "author"]
        read_only_fields = ["author"]
