import json

from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from apps.webhooks.forms import IdentityTriggerForm
from apps.webhooks.models import IncomingWebhook
from apps.webhooks.webhooks import handle_identity_webhook


@csrf_exempt
def identity_webhook_receiver(request: HttpRequest):
    try:
        data = request.body.decode("utf-8")
        handle_identity_webhook(data)
    except Exception as e:
        return HttpResponse(
            {"error": "Failed to decode webhook data."},
            status=500,
            content_type="application/json",
        )

    return HttpResponse()


def trigger_identities_request(request: HttpRequest):
    form = IdentityTriggerForm(data=request.POST)
    form.is_valid()
    form.save()
    return HttpResponseRedirect(reverse("webhooks-home"))


class WebhooksTemplateView(TemplateView):
    template_name = "webhooks/webhooks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = IdentityTriggerForm()
        context["last_incoming_webhook"] = IncomingWebhook.objects.first()
        return context
