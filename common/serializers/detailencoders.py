from common.json import ModelEncoder

from events.models import (
    Conference,
    Location,
    State,
)

from presentations.models import Presentation
from attendees.models import Attendee
from .listencoders import ConferenceListEncoder


class AttendeeDetailEncoder(ModelEncoder):
    model = Attendee
    properties = [
        "email",
        "name",
        "company_name",
        "created",
        "conference",
    ]
    encoders = {
        "conference": ConferenceListEncoder(),
    }


class StateEncoder(ModelEncoder):
    model = State
    properties = [
        "abbreviation",
        "name",
    ]


class ConferenceDetailEncoder(ModelEncoder):
    model = Conference
    properties = [
        "name",
        "description",
        "max_presentations",
        "max_attendees",
        "starts",
        "ends",
        "created",
        "updated",
    ]


class LocationDetailEncoder(StateEncoder, ModelEncoder):
    model = Location
    properties = ["name", "city", "room_count", "created", "updated", "state"]

    encoders = {
        "state": StateEncoder(),
    }


class PresentationDetailEncoder(ModelEncoder):
    model = Presentation
    properties = [
        "title",
        "synopsis",
    ]
