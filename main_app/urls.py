from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),  # home is landing page
    path("accounts/signin/", views.Signin.as_view(), name="signin"),
    path("accounts/signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("parks/", views.park_list, name="park_list"),
    path("parks/<int:park_id>/", views.park_detail, name="park_detail"),
    path(
        "parks/<int:park_id>/add",
        views.UserParkInfoCreate.as_view(),
        name="add_user_park",
    ),
    path(
        "parks/<int:park_id>/add/<int:photo_id>",
        views.UserParkInfoCreate.as_view(),
        name="add_user_park_with_photo",
    ),
    path(
        "userparks/<int:pk>/edit",
        views.UserParkInfoUpdate.as_view(),
        name="edit_user_park",
    ),
    path(
        "userparks/<int:pk>/delete/",
        views.UserParkInfoDelete.as_view(),
        name="delete_user_park",
    ),
    path(
        "userparks/<int:pk>", views.UserParkInfoDetail.as_view(), name="userpark_detail"
    ),
    path(
        "userphotos/<int:pk>/delete/",
        views.UserPhotoDelete.as_view(),
        name="delete_user_photo",
    ),
]
