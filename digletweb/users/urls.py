from django.urls import path

from digletweb.users import views

app_name = "users"

urlpatterns = [
    path("avatar/", views.UserAvatarUpload.as_view(), name="avatar_upload"),
    path("background/", views.UserBackgroundUpload.as_view(), name="background_upload"),
    path("profile/<str:username>/", views.UserProfile.as_view(), name="profile"),
    path("my_profile/", views.MyProfile.as_view(), name="my_profile"),
]
