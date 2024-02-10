from pydantic import BaseModel
from typing import Optional
from app.dto.address_dto import AddressDto
from app.util.google_maps_manager import GoogleMapsInfo


class CreateAddressRequest(BaseModel):
    address_line_one: str
    address_line_two: Optional[str] = None
    address_line_three: Optional[str] = None
    address_line_four: Optional[str] = None
    city: str
    state_or_province: str
    zip_or_postal: str
    country_code: str
    latitude: float
    longitude: float

    def address(self) -> str:
        """Concatenate non-empty address lines."""
        arr = [
            self.address_line_one,
            self.address_line_two,
            self.address_line_three,
            self.address_line_four
        ]
        address_parts = [address for address in arr if
                         address]
        return " ".join(address_parts)


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
    """Create an AddressResponse from CreateAddressRequest and GoogleMapsInfo."""
    return AddressResponse(
        **create_address.dict(),
        **google_maps_info.dict()
    )


def from_dto(dto: AddressDto) -> AddressResponse:
    """Converts a DTO object to its API representation."""
    return AddressResponse(**dto.dict())