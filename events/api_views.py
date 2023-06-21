from django.http import JsonResponse

from .models import Conference, Location
from common.serializers.detailencoders import (
    ConferenceDetailEncoder,
    LocationDetailEncoder,
)
from common.serializers.listencoders import (
    ConferenceListEncoder,
    LocationListEncoder,
)


def api_list_conferences(request):
    conferences = Conference.objects.all()
    return JsonResponse(
        conferences,
        encoder=ConferenceListEncoder,
        safe=False,
    )


def api_show_conference(request, id):
    conference = Conference.objects.get(id=id)
    return JsonResponse(
        conference,
        encoder=ConferenceDetailEncoder,
        safe=False,
    )


def api_list_locations(request):
    loc = Location.objects.all()
    return JsonResponse(
        loc,
        encoder=LocationListEncoder,
        safe=False,
    )


def api_show_location(request, id):
    location = Location.objects.get(id=id)
    return JsonResponse(
        location,
        encoder=LocationDetailEncoder,
        safe=False,
    )
