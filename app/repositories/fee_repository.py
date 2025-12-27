
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.fee import FeeDB

class FeeRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_fee(self, student_id: str, amount: float) -> FeeDB:
        fee = FeeDB(
            student_id=student_id,
            amount=amount,
            status="PAID"
        )
        self.session.add(fee)
        await self.session.commit()
        return fee
