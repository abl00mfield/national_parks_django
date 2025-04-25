from django.contrib import admin

from .models import NationalPark, UserParkInfo

admin.site.register(NationalPark)
admin.site.register(UserParkInfo)
# Register your models here.
