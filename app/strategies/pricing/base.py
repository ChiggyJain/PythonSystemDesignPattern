
from abc import ABC, abstractmethod

class PricingStrategy(ABC):

    @abstractmethod
    async def calculate(self, base_amount: float) -> float:
        pass
