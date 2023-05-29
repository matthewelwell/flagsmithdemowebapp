from django.urls import path

from apps.webhooks import views


urlpatterns = [
    path("", views.WebhooksTemplateView.as_view(), name="webhooks-home"),
    path("identity-receiver", views.identity_webhook_receiver, name="webhooks-identity-receiver"),
    path("identities-trigger", views.trigger_identities_request, name="webhooks-identities-trigger"),
]
