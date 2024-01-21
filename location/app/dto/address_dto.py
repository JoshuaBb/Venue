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

    def __init__(self, d: dict):
        self.__dict__.update(d)
