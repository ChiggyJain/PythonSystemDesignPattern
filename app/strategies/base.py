
from abc import ABC, abstractmethod

class PricingStrategy(ABC):

    @abstractmethod
    async def calculate_price(self, base_price: float) -> float:
        pass
