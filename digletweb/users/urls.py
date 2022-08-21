from django.urls import path

from digletweb.users import views

app_name = "users"

urlpatterns = [path("avatar/", views.UserAvatarUpload.as_view(), name="avatar_upload")]
