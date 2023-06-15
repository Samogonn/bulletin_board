from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AnnouncementForm, ResponseForm
from .models import Announcement, Response
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


class AddResponseView(CreateView):
    model = Response
    form_class = ResponseForm
    template_name = "add_response.html"
    success_url = reverse_lazy("board")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.announcement_id = self.kwargs["pk"]
        return super().form_valid(form)


class UpdateAnnouncementView(LoginRequiredMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "update_announcement.html"


class DeleteAnnouncementView(DeleteView):
    model = Announcement
    template_name = "delete_announcement.html"
    success_url = reverse_lazy("board")


class DeleteResponseView(DeleteView):
    model = Response
    template_name = "delete_response.html"
    success_url = reverse_lazy("profile")
