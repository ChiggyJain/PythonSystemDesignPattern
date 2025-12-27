
from app.repositories.fee_repository import FeeRepository
from app.services.fee_service import FeeService
from app.queue.event_publisher import EventPublisher
from app.services.notification_service import NotificationService
from app.factories.notification_factory import NotificationFactory
from app.strategies.notification_strategy import NotificationStrategy

class ExamFeeFacade:
    """
    Facade hides all complexity of:
    - DB
    - Queue
    - Notification
    - Strategy + Factory + Adapter
    """

    def __init__(self, fee_repo: FeeRepository):
        self.fee_service = FeeService(
            fee_repo=fee_repo,
            publisher=EventPublisher()
        )
        self.notification_strategy = NotificationStrategy()

    async def pay_exam_fee(
        self,
        student_id: str,
        amount: float,
    ):
        # 1️⃣ Core business operation
        fee = await self.fee_service.submit_exam_fee(
            student_id=student_id,
            amount=amount
        )

        # 2️⃣ Decide notification behavior
        channel = self.notification_strategy.choose_channel("FEE_PAID")

        # 3️⃣ Notify asynchronously (adapter handles retry + CB)
        adapter = NotificationFactory.get_adapter(channel)
        notification_service = NotificationService(adapter)

        await notification_service.notify(
            to=student_id,
            message=f"Exam fee paid: {amount}"
        )

        return fee
