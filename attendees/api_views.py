import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Attendee
from events.models import Conference

from common.serializers.listencoders import AttendeeListEncoder
from common.serializers.detailencoders import AttendeeDetailEncoder


@require_http_methods(["GET", "POST", "DELETE", "PUT"])
def api_list_attendees(request, conference_id):
    if request.method == "GET":
        attendees = Attendee.objects.filter(conference__id=conference_id)
        return JsonResponse(
            attendees,
            encoder=AttendeeListEncoder,
            safe=False,
        )
    elif request.method == "POST":
        content = json.loads(request.body)
        try:
            conference = Conference.objects.get(id=conference_id)
            content["conference"] = conference
        except Conference.DoesNotExist:
            return JsonResponse(
                {"message": "conference don't exist"},
                status=400,
            )

        attendee = Attendee.objects.create(**content)
        return JsonResponse(
            attendee,
            encoder=AttendeeDetailEncoder,
            safe=False,
        )


def api_show_attendee(request, id):
    attendee = Attendee.objects.get(id=id)
    return JsonResponse(
        attendee,
        encoder=AttendeeDetailEncoder,
        safe=False,
    )


def api_create_badge(request, id):
    if request.method == "POST":
        Attendee.objects.get(id=id).create_badge()
        return JsonResponse(
            f"badge created for: {Attendee.objects.get(id=id).name}",
            status=201,
            safe=False,
        )
