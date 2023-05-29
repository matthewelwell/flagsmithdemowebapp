class Account:
    id: int
    balance: int
    notification_email: str

    def __init__(self, id: int, balance: int, notification_email: str = None):
        self.id = id
        self.balance = balance
        self.notification_email = (
            notification_email or f"matthew.elwell+account_id#{id}@flagsmith.com"
        )


ACCOUNTS = {
    1: Account(1, 12500),
    2: Account(2, 4500),
    3: Account(3, 800976),
    4: Account(4, 67544),
    5: Account(5, 50765),
    6: Account(6, 53778),
    7: Account(7, 14999),
    8: Account(8, 1290541),
    9: Account(9, 98653),
    10: Account(10, 10909),
}
