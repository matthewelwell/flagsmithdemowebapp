import json
import typing
from dataclasses import dataclass, field

from django.db import models


@dataclass
class IdentityFlagInformation:
    name: str
    enabled: bool
    value: typing.Any = None


@dataclass
class IdentityFlagsInformation:
    identifier: str
    flags: list[IdentityFlagInformation] = field(default_factory=list)


class IncomingWebhook(models.Model):
    raw = models.JSONField()
    received_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-received_at",)

    @property
    def content(self) -> IdentityFlagsInformation:
        json_data = json.loads(self.raw)
        return IdentityFlagsInformation(
            identifier=json_data["identity"],
            flags=[
                IdentityFlagInformation(
                    enabled=flag["enabled"],
                    value=flag["feature_state_value"],
                    name=flag["feature"]["name"],
                )
                for flag in json_data["flags"]
            ],
        )
