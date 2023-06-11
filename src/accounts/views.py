from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import SignUpForm, EditProfileForm
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("account_login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("board")

    def get_object(self):
        return self.request.user


class UserView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/index.html"
