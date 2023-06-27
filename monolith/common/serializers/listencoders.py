from ..json import ModelEncoder

from events.models import (
    Location,
    Conference,
)

from presentations.models import (
    Presentation,
    Status,
)


class ConferenceListEncoder(ModelEncoder):
    model = Conference
    properties = [
        "name",
    ]


class StatusEncoder(ModelEncoder):
    model = Status
    properties = [
        "name",
    ]


class LocationListEncoder(ModelEncoder):
    model = Location
    properties = ["name"]


class PresentationListEncoder(ModelEncoder):
    conferences = ConferenceListEncoder
    model = Presentation
    properties = [
        "presenter_name",
        "company_name",
        "presenter_email",
        "title",
        "synopsis",
        "created",
        "status",
        "conference",
        "picture_url",
    ]
    encoders = {
        "status": StatusEncoder(),
        "conference": ConferenceListEncoder(),
    }
