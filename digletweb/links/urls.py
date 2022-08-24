from django.urls import path

from digletweb.links import views

app_name = "links"

urlpatterns = [
    path(
        "<int:id>/related/",
        views.RelatedLinkListCreate.as_view(),
        name="related_link_list_create",
    ),
    path(
        "<int:parent_id>/related/<int:related_id>/",
        views.RelatedLinkRetrieveUpdateDestroy.as_view(),
        name="related_link_retrieve_update_destroy",
    ),
]
