class NotificationStrategy:
    def choose_channel(self, event: str) -> str:
        if event == "FEE_PAID":
            return "email"
        return "sms"
