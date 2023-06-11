from django.urls import path
from .views import (
    BoardView,
    AnnouncementDetailView,
    AddAnnouncementView,
    UpdateAnnouncementView,
    DeleteAnnouncementView,
)


urlpatterns = [
    path("", BoardView.as_view(), name="board"),
    path(
        "announcements/<int:pk>",
        AnnouncementDetailView.as_view(),
        name="announcement_details",
    ),
    path("add_announcement/", AddAnnouncementView.as_view(), name="add_announcement"),
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
]
