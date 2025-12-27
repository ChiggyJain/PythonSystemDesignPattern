
import asyncio
from app.notifications.base import NotificationSender

class EmailNotification(NotificationSender):

    async def send(self, to: str, message: str) -> None:
        # simulate SMTP I/O
        await asyncio.sleep(0.2) 
        print(f"📧 Email sent to {to}: {message}")
