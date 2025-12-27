
from app.strategies.pricing.student_tuition import StudentTuitionPricing
from app.strategies.pricing.staff_tuition import StaffTuitionPricing
from app.strategies.pricing.guest_tuition import GuestTuitionPricing
from app.strategies.pricing.base import PricingStrategy

class PricingStrategyFactory:

    @staticmethod
    def get_strategy(user_role: str, fee_type: str) -> PricingStrategy:
        if fee_type == "tuition":
            if user_role == "student":
                return StudentTuitionPricing()
            if user_role == "staff":
                return StaffTuitionPricing()
            return GuestTuitionPricing()

        raise ValueError("Unsupported fee type")
