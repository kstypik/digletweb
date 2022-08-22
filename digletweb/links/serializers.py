from rest_framework import serializers

from digletweb.links.models import Link, RelatedLink


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "title", "slug", "domain", "description", "thumbnail", "author"]
        read_only_fields = ["author"]


class RelatedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedLink
        fields = ["url", "parent", "title", "author", "created", "thumbnail", "domain"]
        read_only_fields = ["author", "parent"]
