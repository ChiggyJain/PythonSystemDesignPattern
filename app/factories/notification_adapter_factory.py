
from app.adapters.aws_ses_adapter import AwsSesAdapter
from app.adapters.twilio_adapter import TwilioAdapter
from app.ports.notification_port import NotificationPort

class NotificationAdapterFactory:

    @staticmethod
    def get_adapter(channel: str) -> NotificationPort:
        if channel == "email":
            return AwsSesAdapter()
        if channel == "sms":
            return TwilioAdapter()

        raise ValueError("Unsupported notification channel")
