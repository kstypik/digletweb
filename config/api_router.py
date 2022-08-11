from django.conf import settings

from rest_framework.routers import DefaultRouter, SimpleRouter

from digletweb.links.views import LinkViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("links", LinkViewSet)


app_name = "api"
urlpatterns = router.urls
