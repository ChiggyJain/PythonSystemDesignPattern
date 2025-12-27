
import asyncio
from app.strategies.base import PricingStrategy

class GuestPricing(PricingStrategy):

    async def calculate_price(self, base_price: float) -> float:
        await asyncio.sleep(0.05)
        return base_price
