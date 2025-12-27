
import asyncio
from app.notifications.base import NotificationSender

class SMSNotification(NotificationSender):

    async def send(self, to: str, message: str) -> None:
        # simulate SMS gateway
        await asyncio.sleep(0.1) 
        print(f"📱 SMS sent to {to}: {message}")
