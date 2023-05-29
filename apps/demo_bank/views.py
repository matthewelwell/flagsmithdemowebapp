from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from apps.demo_bank.accounts import ACCOUNTS
from apps.demo_bank.forms import TransferForm
from apps.feature_flags.feature_flags import get_flagsmith


class DemoBankHomeTemplateView(TemplateView):
    template_name = "demo_bank/demo_bank_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flags = get_flagsmith().get_environment_flags()
        context["enable_money_transfer"] = flags.is_feature_enabled("money_transfer")
        context["account"] = ACCOUNTS.get(int(self.request.GET.get("account_id", 1)))
        return context


class DemoBankTransferTemplateView(FormView):
    template_name = "demo_bank/demo_bank_transfer.html"
    form_class = TransferForm

    def get_success_url(self):
        return "%s?account_id=%s" % (
            reverse("demo-bank-home"),
            self.get_form().data["from_account_id"],
        )

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def handle_transfer_request(request: HttpRequest) -> HttpResponse:
    form = TransferForm(data=request.POST)
    form.is_valid()
    form.save()
    return HttpResponseRedirect(
        "%s?account_id=%s"
        % (reverse("demo-bank-home"), form.cleaned_data["from_account_id"])
    )
