

import asyncio
from app.ports.notification_port import NotificationPort

class TwilioAdapter(NotificationPort):

    async def send(self, to: str, message: str) -> None:
        await asyncio.sleep(0.1)  # simulate Twilio SMS API
        print(f"[Twilio] SMS sent to {to}: {message}")
