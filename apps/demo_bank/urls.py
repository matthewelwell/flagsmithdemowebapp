from django.urls import path

from apps.demo_bank import views

urlpatterns = [
    path("", views.DemoBankHomeTemplateView.as_view(), name="demo-bank-home"),
    path("transfer/", views.DemoBankTransferTemplateView.as_view(), name="demo-bank-transfer"),
    path("transfer/", views.DemoBankTransferTemplateView.as_view(), name="demo-bank-transfer"),
]
