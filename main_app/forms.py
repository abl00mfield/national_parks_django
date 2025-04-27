from django import forms
from .models import UserParkInfo


class UserParkInfoForm(forms.ModelForm):
    class Meta:
        model = UserParkInfo
        fields = ["notes", "activities", "rating", "visited"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4}),
            "activities": forms.Textarea(attrs={"rows": 2}),
        }


class UserParkInfoEditForm(forms.ModelForm):
    class Meta:
        model = UserParkInfo
        fields = ["notes", "activities", "rating", "visited", "user_photo"]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 4}),
            "activities": forms.Textarea(attrs={"rows": 2}),
        }
