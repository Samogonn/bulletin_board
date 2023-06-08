from django import forms
from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ("title", "title_tag", "author", "text")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }
