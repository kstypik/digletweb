from django.shortcuts import get_object_or_404

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from vote.views import VoteMixin

from digletweb.core.permissions import IsAuthorOrReadOnly
from digletweb.links.models import Link, RelatedLink
from digletweb.links.serializers import LinkSerializer, RelatedLinkSerializer


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
        serializer.save(parent=parent_link)
