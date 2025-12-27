
import asyncio
from app.strategies.pricing.base import PricingStrategy

class StudentTuitionPricing(PricingStrategy):

    async def calculate(self, base_amount: float) -> float:
        await asyncio.sleep(0.05)  # simulate rule lookup / Redis
        return base_amount * 0.5
