from pydantic import BaseModel
from typing import Optional
from app.dto.address_dto import AddressDto


def from_dto(dto: AddressDto):
    address = Address()
    address.location_id = dto.location_id


class Address(BaseModel):
    location_id: Optional[int] = None
    address_line_one: Optional[str] = None
    address_line_two: Optional[str] = None
    address_line_three: Optional[str] = None
    address_line_four: Optional[str] = None
    city: Optional[str] = None
    state_or_province: Optional[str] = None
    zip_or_postal: Optional[str] = None
    country_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


