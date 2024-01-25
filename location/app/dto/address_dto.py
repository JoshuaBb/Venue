from typing import Optional


class AddressDto:
    address_id: int
    address_line_one: str
    address_line_two: Optional[str]
    address_line_three: Optional[str]
    address_line_four: Optional[str]
    city: str
    state_or_province: str
    zip_or_postal: str
    country_code: str
    latitude: float
    longitude: float
    place_id: str

    def __init__(self):
        pass

def address_dto_from_dict(d: dict) -> AddressDto:
    dto = AddressDto()
    dto.__dict__.update(d)
    return dto
