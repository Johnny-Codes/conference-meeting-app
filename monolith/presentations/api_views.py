import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from common.serializers.detailencoders import PresentationDetailEncoder
from common.serializers.listencoders import PresentationListEncoder
from .models import Presentation
from events.models import Conference


@require_http_methods(["GET", "POST"])
def api_list_presentations(request, conference_id):
    if request.method == "GET":
        presentations = Presentation.objects.filter(conference=conference_id)

        return JsonResponse(
            presentations,
            encoder=PresentationDetailEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        try:
            conf = Conference.objects.get(id=conference_id)
            content["conference"] = conf
        except Conference.DoesNotExist:
            return JsonResponse(
                {"message": "conference don't exist"},
                status=400,
            )
        presentation = Presentation.create(**content)
        return JsonResponse(
            {"presentation": presentation},
            encoder=PresentationDetailEncoder,
        )


def api_show_presentation(request, id):
    p = Presentation.objects.get(id=id)
    return JsonResponse(
        p,
        encoder=PresentationListEncoder,
        safe=False,
    )
