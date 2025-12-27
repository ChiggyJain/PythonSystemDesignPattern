
from app.strategies.student import StudentPricing
from app.strategies.staff import StaffPricing
from app.strategies.guest import GuestPricing
from app.strategies.base import PricingStrategy
from app.factories.pricing_strategy_factory import PricingStrategyFactory


class PricingService:

    def _get_strategy(self, user_type: str) -> PricingStrategy:
        if user_type == "student":
            return StudentPricing()
        if user_type == "staff":
            return StaffPricing()
        return GuestPricing()

    async def get_final_price(self, user_type: str, base_price: float) -> float:
        strategy = self._get_strategy(user_type)
        return await strategy.calculate_price(base_price)

    async def calculate_fee(self, user_role: str, fee_type: str, base_amount: float,) -> float:
        strategy = PricingStrategyFactory.get_strategy(
            user_role=user_role, fee_type=fee_type,
        )
        return await strategy.calculate(base_amount)
