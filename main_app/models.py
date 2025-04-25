from django.db import models
from django.contrib.auth.models import User


class NationalPark(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    established_date = models.DateField(null=True, blank=True)
    area_in_acres = models.FloatField(null=True, blank=True)
    website = models.URLField(blank=True)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class UserParkInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    park = models.ForeignKey(
        NationalPark, on_delete=models.CASCADE, related_name="user_infos"
    )

    notes = models.TextField(blank=True)
    activities = models.TextField(blank=True)
    rating = models.IntegerField(
        null=True, blank=True, choices=[(i, i) for i in range(1, 6)]
    )
    visited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_photo = models.ImageField(upload_to="user_photos/", null=True, blank=True)

    class Meta:
        unique_together = ("user", "park")

    def __str__(self):
        return f"{self.user.username}'s info for {self.park.name}"


# Create your models here.
