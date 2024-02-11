# app/models/order.py

from typing import List
from pydantic import BaseModel
from uuid import UUID, uuid4
from app.models.address import AddressDto


class OrderDto(BaseModel):
    id: UUID
    username: str
  #  user_id: UUID
    deliver_address: AddressDto
    #products: List[ProductDto]
