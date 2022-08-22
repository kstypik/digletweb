from rest_framework import viewsets

from vote.views import VoteMixin

from digletweb.core.permissions import IsAuthorOrReadOnly
from digletweb.links.models import Link
from digletweb.links.serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet, VoteMixin):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
