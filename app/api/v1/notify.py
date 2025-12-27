
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.notification_service import NotificationService
from app.api.deps import get_notification_service

router = APIRouter()

class NotifyRequest(BaseModel):
    to: str
    message: str
    channel: str

@router.post("/notify")
async def send_notification(payload: NotifyRequest):
    service = get_notification_service(payload.channel)
    await service.notify(payload.to, payload.message)
    return {"status": "sent"}
