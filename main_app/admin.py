from django.contrib import admin

from .models import NationalPark, UserParkInfo, ParkPhoto

admin.site.register([NationalPark, UserParkInfo, ParkPhoto])

# Register your models here.
