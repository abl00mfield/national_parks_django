from django.db import models


class NationalPark(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    established_date = models.DateField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


# Create your models here.
