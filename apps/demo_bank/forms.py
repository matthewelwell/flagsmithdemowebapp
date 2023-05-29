from django import forms

from apps.demo_bank.demo_bank_service import transfer_money


class TransferForm(forms.Form):
    from_account_id = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    to_account_id = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    amount = forms.IntegerField(
        min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    def save(self):
        transfer_money(
            self.cleaned_data["from_account_id"],
            self.cleaned_data["to_account_id"],
            self.cleaned_data["amount"],
        )
