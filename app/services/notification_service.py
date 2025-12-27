
from app.factories.notification_factory import NotificationFactory

class NotificationService:

    async def notify(self, channel: str, to: str, message: str):
        sender = NotificationFactory.get_sender(channel)
        await sender.send(to, message)



from app.ports.notification_port import NotificationPort

class NotificationService:

    def __init__(self, notifier: NotificationPort):
        self.notifier = notifier

    async def notify(self, to: str, message: str) -> None:
        await self.notifier.send(to, message)



