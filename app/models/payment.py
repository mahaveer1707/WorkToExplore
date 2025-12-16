from pydantic import BaseModel
from uuid import UUID

class PaymentCreate(BaseModel):
    amount: float
    currency: str

class Payment(PaymentCreate):
    id: UUID
    status: str
