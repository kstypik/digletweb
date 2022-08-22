from django.urls import path

from digletweb.links import views

app_name = "links"

urlpatterns = [
    path(
        "<int:id>/related/",
        views.RelatedLinkListCreate.as_view(),
        name="related_link_list_create",
    ),
]
