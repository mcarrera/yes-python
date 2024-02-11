# app/models/address.py

from pydantic import BaseModel

class AddressDto(BaseModel):
    street_address: str
    city: str
    state: str
    postal_code: str
    country: str
   # id: UUID
