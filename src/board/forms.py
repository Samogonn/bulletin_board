from django import forms
from .models import Announcement, Response


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = (
            "title",
            "title_tag",
            "author",
            "category",
            "text",
            "image",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "unique_id",
                    "type": "hidden",
                }
            ),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.SelectMultiple(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ("author", "text")

        widgets = {
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "unique_id",
                    "type": "hidden",
                }
            ),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }
