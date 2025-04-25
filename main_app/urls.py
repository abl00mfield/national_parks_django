from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),  # home is landing page
    path("accounts/signin/", views.Signin.as_view(), name="signin"),
    path("accounts/signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("parks/", views.park_list, name="park_list"),
]
