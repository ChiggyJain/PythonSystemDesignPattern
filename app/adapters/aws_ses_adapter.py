

import asyncio
from app.ports.notification_port import NotificationPort

class AwsSesAdapter(NotificationPort):

    async def send(self, to: str, message: str) -> None:
        await asyncio.sleep(0.2)  # simulate AWS SES network I/O
        print(f"[AWS SES] Email sent to {to}: {message}")
