from django.urls import path

from .api_views import (
    api_list_attendees,
    api_show_attendee,
    api_create_badge,
)

urlpatterns = [
    path(
        "conferences/<int:conference_vo_id>/attendees/",
        api_list_attendees,
        name="api_list_attendees",
    ),
    path(
        "attendees/<int:id>/",
        api_show_attendee,
        name="api_show_attendee",
    ),
    path(
        "attendees/<int:id>/create_badge/",
        api_create_badge,
        name="api_create_badge",
    ),
    path(
        "attendees/",
        api_list_attendees,
        name="api_create_attendees",
    ),
]
