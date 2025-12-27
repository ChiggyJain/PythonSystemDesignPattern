
from app.notifications.base import NotificationSender
from app.notifications.email import EmailNotification
from app.notifications.sms import SMSNotification


class NotificationFactory:

    @staticmethod
    def get_sender(channel: str) -> NotificationSender:
        if channel == "email":
            return EmailNotification()
        if channel == "sms":
            return SMSNotification()
        raise ValueError(f"Unsupported notification channel: {channel}")
