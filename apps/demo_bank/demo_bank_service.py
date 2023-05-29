from django.core.mail import send_mail

from apps.demo_bank.accounts import ACCOUNTS, Account
from apps.feature_flags.feature_flags import is_feature_enabled


def transfer_money(from_account_id: int, to_account_id: int, amount: int) -> None:
    from_account = ACCOUNTS[from_account_id]
    to_account = ACCOUNTS[to_account_id]

    if is_feature_enabled("send_transfer_notifications"):
        _send_transfer_notifications(from_account, to_account, amount)

    _do_transfer(from_account, to_account, amount)


def _do_transfer(from_account: Account, to_account: Account, amount: int) -> None:
    from_account.balance -= amount
    to_account.balance += amount


def _send_transfer_notifications(from_account: Account, to_account: Account, amount: int):
    """
    Function designed to send relevant notifications to from / to account.
    """
    send_mail(
        subject="You've sent money",
        message=f"You've sent £{amount:,} to account #{to_account.id}",
        recipient_list=[from_account.notification_email],
        from_email="noreply@demobank.com"
    )
    send_mail(
        subject="You've received money",
        message=f"You've received £{amount:,} from account #{from_account.id}",
        recipient_list=[to_account.notification_email],
        from_email="noreply@demobank.com"
    )
