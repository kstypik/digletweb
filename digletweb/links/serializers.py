from rest_framework import serializers

from digletweb.links.models import Comment, Link, RelatedLink


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "title", "slug", "domain", "description", "thumbnail", "author"]
        read_only_fields = ["author"]


class RelatedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedLink
        fields = [
            "id",
            "url",
            "parent",
            "title",
            "author",
            "created",
            "thumbnail",
            "domain",
        ]
        read_only_fields = ["author", "parent"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "link", "author", "message", "created"]
        read_only_fields = ["author", "link"]


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "parent", "author", "message", "created"]
        read_only_fields = ["author", "parent"]
