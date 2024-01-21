from pydantic import BaseModel
from typing import Optional
from app.dto.address_dto import AddressDto
from app.util.google_maps_manager import GoogleMapsInfo

class CreateAddressRequest(BaseModel):
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


class AddressResponse(BaseModel):
    address_id: Optional[int] = None
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




def to_address(create_address: CreateAddressRequest, google_maps_info: GoogleMapsInfo) -> AddressResponse:
    # TODO: I am sure there is a better way
    address = AddressResponse()
    address.__dict__.update(create_address.__dict__)
    address.__dict__.update(google_maps_info.__dict__)
    return address

def from_dto(dto: AddressDto) -> AddressResponse:
    """Converts a DTO object to its API representation"""
    address = AddressResponse()
    address.__dict__.update(dto.__dict__)
    return address
