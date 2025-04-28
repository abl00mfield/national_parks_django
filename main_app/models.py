from django.db import models
from django.contrib.auth.models import User
import os
from cloudinary_storage.storage import MediaCloudinaryStorage


class NationalPark(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class ParkPhoto(models.Model):
    park = models.ForeignKey(
        NationalPark, on_delete=models.CASCADE, related_name="photos"
    )
    image_url = models.URLField()
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Photo for {self.park.name}"


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
    chosen_photo = models.ForeignKey(
        "ParkPhoto", null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        unique_together = ("user", "park")

    def __str__(self):
        return f"{self.user.username}'s info for {self.park.name}"


class UserPhoto(models.Model):
    user_park_info = models.ForeignKey(
        UserParkInfo, on_delete=models.CASCADE, related_name="user_photos"
    )
    image = models.ImageField(upload_to="user_photos/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Photo for {self.user_park_info.park.name} by {self.user_park_info.user.username}"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
