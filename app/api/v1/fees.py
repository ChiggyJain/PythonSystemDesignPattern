
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.facades.exam_fee_facade import ExamFeeFacade
from app.repositories.fee_repository import FeeRepository
from app.api.deps import get_db

router = APIRouter()

class FeeRequest(BaseModel):
    student_id: str
    amount: float

@router.post("/exam-fee")
async def pay_exam_fee(
    payload: FeeRequest,
    db: AsyncSession = Depends(get_db),
):
    facade = ExamFeeFacade(FeeRepository(db))

    fee = await facade.pay_exam_fee(
        student_id=payload.student_id,
        amount=payload.amount
    )

    return {
        "status": "success",
        "fee_id": fee.id
    }
