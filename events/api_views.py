import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Conference, Location, State
from common.serializers.detailencoders import (
    ConferenceDetailEncoder,
    LocationDetailEncoder,
)
from common.serializers.listencoders import (
    ConferenceListEncoder,
    LocationListEncoder,
)


@require_http_methods(["GET", "POST"])
def api_list_conferences(request):
    if request.method == "GET":
        conferences = Conference.objects.all()
        return JsonResponse(
            {"conferences": conferences},
            encoder=ConferenceListEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        try:
            location = Location.objects.get(id=content["location"])
            content["location"] = location
        except Location.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Location"},
                status=400,
            )
        conference = Conference.objects.create(**content)
        return JsonResponse(
            {"conference": conference},
            encoder=ConferenceDetailEncoder,
            safe=False,
        )


@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_conference(request, id):
    if request.method == "GET":
        conference = Conference.objects.get(id=id)
        return JsonResponse(
            {"conference": conference},
            encoder=ConferenceDetailEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        try:
            count, _ = Conference.objects.get(id=id).delete()
            return JsonResponse({"deleted": count > 0})
        except Conference.DoesNotExist:
            return JsonResponse(
                {"message": "Conference does not exist"},
                status=400,
            )
    else:
        content = json.loads(request.body)
        try:
            conf = Conference.objects.filter(id=id)
            conf.update(**content)
        except Conference.DoesNotExist:
            return JsonResponse(
                {"message": "conference does not exist"},
                status=400,
            )
        conference = Conference.objects.get(id=id)
        return JsonResponse(
            conference,
            encoder=ConferenceDetailEncoder,
            safe=False,
        )


@require_http_methods(["GET", "POST"])
def api_list_locations(request):
    if request.method == "GET":
        loc = Location.objects.all()
        return JsonResponse(
            {"locations": loc},
            encoder=LocationListEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        try:
            state = State.objects.get(abbreviation=content["state"])
            content["state"] = state
        except State.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid state abbreviation"},
                status=400,
            )
        loc = Location.objects.create(**content)
        return JsonResponse(
            loc,
            encoder=LocationDetailEncoder,
            safe=False,
        )


@require_http_methods(["GET", "PUT", "DELETE"])
def api_show_location(request, id):
    if request.method == "GET":
        try:
            location = Location.objects.get(id=id)
            return JsonResponse(
                {"location": location},
                encoder=LocationDetailEncoder,
                safe=False,
            )
        except Location.DoesNotExist:
            return JsonResponse(
                {"message": "Location does not exist"},
                status=400,
            )
    elif request.method == "DELETE":
        try:
            count, _ = Location.objects.get(id=id).delete()
            return JsonResponse({"deleted": count > 0})
        except Location.DoesNotExist:
            return JsonResponse(
                {"message": "Location does not exist"},
                status=400,
            )
    else:
        content = json.loads(request.body)
        try:
            state = State.objects.get(abbreviation=content["state"])
            content["state"] = state
        except State.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid state abbreviation"},
                status=400,
            )
        try:
            location = Location.objects.filter(id=id)
            location.update(**content)
        except Location.DoesNotExist:
            return JsonResponse({"message": "you suck"})
        location = Location.objects.get(id=id)
        return JsonResponse(
            location,
            encoder=LocationDetailEncoder,
            safe=False,
        )
