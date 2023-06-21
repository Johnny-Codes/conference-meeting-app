from django.db import models
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
        verbose_name_plural = "statuses"


class Presentation(models.Model):
    presenter_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    presenter_email = models.EmailField()

    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(
        Status,
        related_name="presentations",
        on_delete=models.PROTECT,
        default="SUBMITTED",
    )

    conference = models.ForeignKey(
        "events.Conference",
        related_name="presentations",
        on_delete=models.CASCADE,
    )

    def get_api_url(self):
        return reverse("api_show_presentation", kwargs={"id": self.id})

    def __str__(self):
        return self.title

    def approve_presentation(self):
        status = Status.objects.get(name="APPROVED")
        self.status = status
        self.save()

    def reject_presentation(self):
        status = Status.objects.get(name="REJECTED")
        self.status = status
        self.save()

    class Meta:
        ordering = ("title",)
