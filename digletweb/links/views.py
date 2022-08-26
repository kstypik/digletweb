from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import generics, viewsets
from rest_framework.decorators import action
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

    def get_queryset(self):
        domain = self.request.query_params.get("domain")
        if self.action == "list" and domain:
            return Link.objects.filter(domain=domain)
        else:
            return super().get_queryset()

    @action(detail=False)
    def hits(self, request):
        time_range_param = request.query_params.get("from")
        time_ranges_map = {
            "day": timedelta(days=1),
            "week": timedelta(days=7),
            "month": timedelta(days=30),
            "year": timedelta(days=365),
        }
        if time_range_param:
            try:
                time_range = timezone.now() + time_ranges_map[time_range_param]
            except KeyError:
                time_range = time_ranges_map["week"]
        links = Link.objects.all().order_by("-vote_score")
        if time_range:
            links = links.filter(created__lte=time_range)
        page = self.paginate_queryset(links)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(links, many=True)
        return Response(serializer.data)


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
