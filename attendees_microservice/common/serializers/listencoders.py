from ..json import ModelEncoder


from attendees.models import (
    Attendee,
    Badge,
)


class BadgeEncoder(ModelEncoder):
    model = Badge
    properties = [
        "created",
    ]


class AttendeeListEncoder(ModelEncoder):
    model = Attendee
    properties = [
        "name",
    ]
    encoders = {}
