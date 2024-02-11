# app/api/order.py

from fastapi import APIRouter
from typing import List
from app.models.order import OrderDto
import uuid

router = APIRouter()

# Dummy order data (replace with actual data later)
dummy_orders = [
    OrderDto(
        id=uuid.UUID('550e8400-e29b-41d4-a716-446655440000'),
        username="john_doe",
        #user_id=uuid.UUID(98765432-9876-5432-9876-543298765432),
        deliver_address={
            "street_address": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "postal_code": "12345",
            "country": "USA",
            # "id": "87654321-8765-4321-8765-432187654321",
        },
       
    ),
    # Add more orders here...
]

@router.get("/orders", response_model=List[OrderDto])
def get_non_deleted_orders():
    return dummy_orders
