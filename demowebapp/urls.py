from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.home.urls")),
    path("webhooks/", include("apps.webhooks.urls")),
    path("demo-bank/", include("apps.demo_bank.urls")),
]
