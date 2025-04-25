from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


def home(request):
    return HttpResponse("<h1>National Parks</h1>")


class SigninView(LoginView):
    template_name = "login.html"


# Create your views here.
