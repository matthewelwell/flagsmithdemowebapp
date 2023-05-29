from django import forms

from apps.feature_flags.feature_flags import get_flagsmith

flagsmith = get_flagsmith()


class IdentityTriggerForm(forms.Form):
    identifier = forms.CharField(max_length=100, label="identifier")

    def save(self, *args, **kwargs):
        flagsmith.get_identity_flags(identifier=self.cleaned_data["identifier"])
