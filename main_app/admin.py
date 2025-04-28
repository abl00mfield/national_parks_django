from django.contrib import admin

from .models import NationalPark, UserParkInfo, ParkPhoto, UserPhoto

admin.site.register([NationalPark, UserParkInfo, ParkPhoto, UserPhoto])

# Register your models here.
