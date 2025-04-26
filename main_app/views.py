from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .models import UserParkInfo, NationalPark, ParkPhoto
from .forms import UserParkInfoForm
from django.urls import reverse_lazy


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


class UserParkInfoCreate(CreateView):
    model = UserParkInfo
    form_class = UserParkInfoForm
    template_name = "user_parkinfo_form.html"

    def form_valid(self, form):
        park = NationalPark.objects.get(id=self.kwargs["park_id"])
        user = self.request.user
        photo_id = self.kwargs.get("photo_id")

        # if the user has already saved this park
        # TODO - add a message to the user that they already added the park
        if UserParkInfo.objects.filter(user=user, park=park).exists():
            return redirect("dashboard")
        else:
            if photo_id:
                try:
                    form.instance.chosen_photo = park.photos.get(id=photo_id)
                except ParkPhoto.DoesNotExist:
                    pass
            else:
                first_photo = park.photos.first()
                if first_photo:
                    form.instance.chosen_photo = first_photo
            form.instance.user = user
            form.instance.park = park

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["park"] = NationalPark.objects.get(id=self.kwargs["park_id"])
        return context

    def get_success_url(self):
        return reverse_lazy("dashboard")
