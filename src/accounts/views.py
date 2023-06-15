from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import SignUpForm, EditProfileForm
from django.urls import reverse_lazy
from board.models import Response

from .filters import ResponseFilter


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("account_login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy("board")

    def get_object(self):
        return self.request.user


class UserView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["responses"] = Response.objects.filter(announcement__author=user)
        context["filter"] = ResponseFilter(
            self.request.GET,
            queryset=Response.objects.filter(announcement__author=user),
        )
        return context
