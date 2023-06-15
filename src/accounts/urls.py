from django.urls import path
from .views import UserRegisterView, UserEditView, UserView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path("register", UserRegisterView.as_view(), name="register"),
    path("profile", UserView.as_view(), name="profile"),
    path("edit_profile", UserEditView.as_view(), name="edit_profile"),
    path("login/", LoginView.as_view(template_name="registration/login.html")),
    path("sign/logout/", LogoutView.as_view(template_name="registration/logout.html")),
]
