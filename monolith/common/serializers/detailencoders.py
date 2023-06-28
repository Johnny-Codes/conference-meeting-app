from common.json import ModelEncoder

from events.models import (
    Conference,
    Location,
    State,
)

from presentations.models import Presentation
from .listencoders import ConferenceListEncoder


class StateEncoder(ModelEncoder):
    model = State
    properties = [
        "abbreviation",
        "name",
    ]


class LocationDetailEncoder(StateEncoder, ModelEncoder):
    model = Location
    properties = [
        "name",
        "city",
        "room_count",
        "created",
        "updated",
        "state",
        "picture_url",
    ]

    encoders = {
        "state": StateEncoder(),
    }


class PresentationDetailEncoder(ModelEncoder):
    model = Presentation
    properties = [
        "presenter_name",
        "company_name",
        "presenter_email",
        "title",
        "synopsis",
        "created",
        "conference",
    ]
    encoders = {
        "conference": ConferenceListEncoder(),
    }

    def get_extra_data(self, o):
        return {"status": o.status.name}


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
