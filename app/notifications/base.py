
from abc import ABC, abstractmethod

# defined abstract
class NotificationSender(ABC):

    @abstractmethod
    async def send(self, to: str, message: str) -> None:
        pass
