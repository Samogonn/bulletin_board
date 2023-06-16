from django.urls import path
from .views import (
    BoardView,
    AnnouncementDetailView,
    AddAnnouncementView,
    UpdateAnnouncementView,
    DeleteAnnouncementView,
    DeleteResponseView,
    AddResponseView,
    accept_response,
)


urlpatterns = [
    path("", BoardView.as_view(), name="board"),
    path(
        "announcements/<int:pk>",
        AnnouncementDetailView.as_view(),
        name="announcement_details",
    ),
    path(
        "add_announcement/",
        AddAnnouncementView.as_view(),
        name="add_announcement",
    ),
    path(
        "announcement/<int:pk>/response",
        AddResponseView.as_view(),
        name="add_response",
    ),
    path(
        "announcement/edit/<int:pk>",
        UpdateAnnouncementView.as_view(),
        name="update_announcement",
    ),
    path(
        "announcement/<int:pk>/delete",
        DeleteAnnouncementView.as_view(),
        name="delete_announcement",
    ),
    path(
        "response/<int:pk>/delete",
        DeleteResponseView.as_view(),
        name="delete_response",
    ),
    path("response/<int:pk>/accept", accept_response, name="accept_response"),
]
