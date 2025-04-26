from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import NationalPark


def home(request):
    return render(request, "landing.html")


def dashboard(request):
    return render(request, "dashboard.html")


class Signin(LoginView):
    template_name = "login.html"


@login_required
def park_list(request):
    parks = NationalPark.objects.all().order_by("name")
    return render(request, "park_list.html", {"parks": parks})


@login_required
def park_detail(request, park_id):
    park = NationalPark.objects.get(id=park_id)
    photos = park.photos.all()
    return render(request, "park_detail.html", {"park": park, "photos": photos})


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
        else:
            error_message = "Invalid sign up - try again"

    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


# Create your views here.
