from django import forms
from .models import UserParkInfo, UserPhoto


class UserParkInfoForm(forms.ModelForm):
    class Meta:
        model = UserParkInfo
        fields = ["notes", "activities", "rating", "visited"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4}),
            "activities": forms.Textarea(attrs={"rows": 2}),
        }


class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ["image", "caption"]
