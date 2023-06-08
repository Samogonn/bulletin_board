from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import AnnouncementForm
from .models import Announcement
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


class BoardView(ListView):
    model = Announcement
    template_name = "board.html"
    ordering = ["-id"]


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "announcement_details.html"


class AddAnnouncementView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "add_announcement.html"


@method_decorator(login_required, name="dispatch")
class UpdateAnnouncementView(UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "update_announcement.html"


class DeleteAnnouncementView(DeleteView):
    model = Announcement
    template_name = "delete_announcement.html"
    success_url = reverse_lazy("board")
