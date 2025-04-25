from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),  # home is landing page
    path("accounts/signin", views.SigninView.as_view(), name="signin"),
    path("accounts/signup", views.signup, name="signup"),
]
