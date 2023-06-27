import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Attendee, ConferenceVO

from common.serializers.listencoders import AttendeeListEncoder
from common.serializers.detailencoders import AttendeeDetailEncoder


@require_http_methods(["GET", "POST", "DELETE", "PUT"])
def api_list_attendees(request, conference_vo_id):
    if request.method == "GET":
        attendees = Attendee.objects.filter(conference=conference_vo_id)
        return JsonResponse(
            attendees,
            encoder=AttendeeListEncoder,
            safe=False,
        )
    elif request.method == "POST":
        content = json.loads(request.body)
        try:
            conference_href = f"/api/conferences/{conference_vo_id}/"
            conference = ConferenceVO.objects.get(import_href=conference_href)
            content["conference"] = conference
        except ConferenceVO.DoesNotExist:
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
    try:
        attendee = Attendee.objects.get(id=id)
        return JsonResponse(
            attendee,
            encoder=AttendeeDetailEncoder,
            safe=False,
        )
    except Attendee.DoesNotExist:
        return JsonResponse({"message": "you don't have data here bud"})


def api_create_badge(request, id):
    if request.method == "POST":
        Attendee.objects.get(id=id).create_badge()
        return JsonResponse(
            f"badge created for: {Attendee.objects.get(id=id).name}",
            status=201,
            safe=False,
        )
