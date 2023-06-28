import json
import pika
import django
import os
import sys
from django.core.mail import send_mail

sys.path.append("")
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "presentation_mailer.settings",
)
django.setup()
print("loaded?")


def send_status_email(ch, method, properties, body):
    body = json.loads(body)
    print("sending email")
    send_mail(
        f"{body['title']} is {body['status']}",
        f"Your presentation {body['title']} is {body['status']}.",
        "admin@conferencego.com",
        [f"{body['presenter_email']}"],
    )


parameters = pika.ConnectionParameters(host="rabbitmq")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue="status")
channel.basic_consume(
    queue="status",
    on_message_callback=send_status_email,
    auto_ack=True,
)
channel.start_consuming()
