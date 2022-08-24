from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from vote.views import VoteMixin

from digletweb.core.permissions import IsAuthorOrReadOnly
from digletweb.links.models import Comment, Link, RelatedLink
from digletweb.links.serializers import (
    CommentSerializer,
    LinkSerializer,
    RelatedLinkSerializer,
    ReplySerializer,
)


class LinkViewSet(viewsets.ModelViewSet, VoteMixin):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RelatedLinkListCreate(generics.ListCreateAPIView):
    serializer_class = RelatedLinkSerializer
    queryset = RelatedLink.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return RelatedLink.objects.filter(parent=self.kwargs["id"])

    def perform_create(self, serializer):
        parent_link = get_object_or_404(Link, id=self.kwargs["id"])
        serializer.save(parent=parent_link, author=self.request.user)


class RelatedLinkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RelatedLinkSerializer
    queryset = RelatedLink.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    lookup_url_kwarg = "related_id"
    lookup_field = "id"

    def get_queryset(self):
        return RelatedLink.objects.filter(parent=self.kwargs["parent_id"])


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(link=self.kwargs["link_id"])

    def perform_create(self, serializer):
        link = get_object_or_404(Link, id=self.kwargs["link_id"])
        serializer.save(link=link, author=self.request.user)


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    lookup_url_kwarg = "comment_id"
    lookup_field = "id"

    def get_queryset(self):
        return Comment.objects.filter(link=self.kwargs["link_id"])


class ReplyListCreate(generics.ListCreateAPIView):
    serializer_class = ReplySerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(
            parent=self.kwargs["parent_id"], link=self.kwargs["link_id"]
        )

    def perform_create(self, serializer):
        parent_comment = get_object_or_404(Comment, id=self.kwargs["parent_id"])
        serializer.save(
            parent=parent_comment, author=self.request.user, link=parent_comment.link
        )


class ReplyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReplySerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    lookup_url_kwarg = "reply_id"
    lookup_field = "id"

    def get_queryset(self):
        return Comment.objects.filter(
            link=self.kwargs["link_id"], parent=self.kwargs["comment_id"]
        )
