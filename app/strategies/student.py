
import asyncio
from app.strategies.base import PricingStrategy

class StudentPricing(PricingStrategy):

    async def calculate_price(self, base_price: float) -> float:
        # simulate rule engine / external call    
        await asyncio.sleep(0.05)  
        return base_price * 0.5
