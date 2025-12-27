
import asyncio
from app.strategies.pricing.base import PricingStrategy

class GuestTuitionPricing(PricingStrategy):

    async def calculate(self, base_amount: float) -> float:
        await asyncio.sleep(0.05)
        return base_amount
