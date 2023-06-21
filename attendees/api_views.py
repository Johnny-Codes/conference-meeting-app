from django.http import JsonResponse

from .models import Attendee
from common.serializers.listencoders import AttendeeListEncoder
from common.serializers.detailencoders import AttendeeDetailEncoder


def api_list_attendees(request, conference_id):
    attendees = Attendee.objects.filter(conference__id=conference_id)
    return JsonResponse(
        attendees,
        encoder=AttendeeListEncoder,
        safe=False,
    )


def api_show_attendee(request, id):
    attendee = Attendee.objects.get(id=id)
    return JsonResponse(
        attendee,
        encoder=AttendeeDetailEncoder,
        safe=False,
    )


def create_badge(request, id):
    if request.method == "POST":
        Attendee.objects.get(id=id).create_badge()
        return JsonResponse("created", status=201)
