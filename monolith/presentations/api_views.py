import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from common.serializers.detailencoders import PresentationDetailEncoder
from common.serializers.listencoders import PresentationListEncoder
from .models import Presentation
from events.models import Conference

import pika


def send_presentation_status_message(presentation, status):
    parameters = pika.ConnectionParameters(host="rabbitmq")
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="status")
    response = {
        "presenter_name": presentation.presenter_name,
        "presenter_email": presentation.presenter_email,
        "title": presentation.title,
        "status": status,
    }
    response = json.dumps(response)
    print(response)
    channel.basic_publish(
        exchange="",
        routing_key="status",
        body=response,
    )

    connection.close()


@require_http_methods(["PUT"])
def api_approve_presentation(request, id):
    presentation = Presentation.objects.get(id=id)
    presentation.approve_presentation()
    send_presentation_status_message(presentation, "APPROVED")
    return JsonResponse(
        presentation,
        encoder=PresentationDetailEncoder,
        safe=False,
    )


@require_http_methods(["PUT"])
def api_reject_presentation(request, id):
    presentation = Presentation.objects.get(id=id)
    presentation.reject_presentation()
    send_presentation_status_message(presentation, "REJECTED")
    return JsonResponse(
        presentation,
        encoder=PresentationDetailEncoder,
        safe=False,
    )


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
