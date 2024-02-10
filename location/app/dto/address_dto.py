"""Module responsible for converting the Result Set from database into valid python object"""
from typing import Optional
from dataclasses import dataclass, asdict

@dataclass
class AddressDto:
    """Class responsible for storing Address level data from the database"""
    address_id: int
    address_line_one: str
    city: str
    state_or_province: str
    zip_or_postal: str
    country_code: str
    latitude: float
    longitude: float
    place_id: str
    address_line_two: Optional[str] = None
    address_line_three: Optional[str] = None
    address_line_four: Optional[str] = None

    def __init__(self):
        pass

    def dict(self) -> dict[str, any]:
        """Converts the class properties into a dict"""
        return asdict(self)

def address_dto_from_dict(d: dict) -> AddressDto:
    """Converts a dict into an AddressDto object"""
    dto = AddressDto()
    dto.__dict__.update(d)
    return dto
