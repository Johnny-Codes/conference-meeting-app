from django.http import JsonResponse
from common.serializers.detailencoders import PresentationDetailEncoder
from common.serializers.listencoders import PresentationListEncoder
from .models import Presentation


def api_list_presentations(request, conference_id):
    presentations = Presentation.objects.filter(conference=conference_id)

    return JsonResponse(
        presentations,
        encoder=PresentationDetailEncoder,
        safe=False,
    )


def api_show_presentation(request, id):
    p = Presentation.objects.get(id=id)
    return JsonResponse(
        p,
        encoder=PresentationListEncoder,
        safe=False,
    )
