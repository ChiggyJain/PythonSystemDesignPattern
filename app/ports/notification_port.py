
from abc import ABC, abstractmethod

class NotificationPort(ABC):

    @abstractmethod
    async def send(self, to: str, message: str) -> None:
        pass
