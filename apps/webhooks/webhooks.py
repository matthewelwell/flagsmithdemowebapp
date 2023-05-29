from apps.webhooks.models import IncomingWebhook


def handle_identity_webhook(incoming_json: str):
    IncomingWebhook.objects.create(raw=incoming_json)
