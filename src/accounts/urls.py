from django.urls import path
from .views import UserRegisterView, UserEditView, UserView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("register", UserRegisterView.as_view(), name="register"),
    path("edit_profile", UserEditView.as_view(), name="edit_profile"),
    path("", UserView.as_view(), name="personal_page"),
    path("login/", LoginView.as_view(template_name="registration/login.html")),
    # path("logout/", LoginView.as_view(template_name="registration/logout.html")),
]
