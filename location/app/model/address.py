from pydantic import BaseModel
from typing import Optional
from app.dto.address_dto import AddressDto
from app.util.google_maps_manager import GoogleMapsInfo


def from_dto(dto: AddressDto):
    """Converts a DTO object to its API representation"""
    address = Address()
    address.location_id = dto.location_id


class CreateAddress(BaseModel):
    address_line_one: str = None
    address_line_two: Optional[str] = None
    address_line_three: Optional[str] = None
    address_line_four: Optional[str] = None
    city: str
    state_or_province: str
    zip_or_postal: str
    country_code: str

    def address(self) -> str:
        var = [address for address in
               [self.address_line_one, self.address_line_two, self.address_line_three, self.address_line_four] if
               address]
        return " ".join(var)


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
    place_id: Optional[str] = None




def to_address(create_address: CreateAddress, google_maps_info: GoogleMapsInfo) -> Address:
    # TODO: I am sure there is a better way
    address = Address()
    address.__dict__.update(create_address.__dict__)
    address.__dict__.update(google_maps_info.__dict__)
    return address
