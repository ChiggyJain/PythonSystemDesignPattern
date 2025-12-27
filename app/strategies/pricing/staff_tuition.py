
import asyncio
from app.strategies.pricing.base import PricingStrategy

class StaffTuitionPricing(PricingStrategy):

    async def calculate(self, base_amount: float) -> float:
        await asyncio.sleep(0.05)
        return base_amount * 0.7
