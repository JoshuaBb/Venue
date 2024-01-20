
class AddressDto:
    address_id: int

    def __init__(self, d: dict):
        self.location_id = d['location_id']
