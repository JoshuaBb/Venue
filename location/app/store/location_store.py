from app.util.database import Db
from app.dto.address_dto import AddressDto
from typing import Optional


class LocationStore:

    def __init__(self, db: Db):
        self.db = db

    async def get_location_by_id(self, location_id: int) -> Optional[AddressDto]:
        return await self.db.query_one("select * from address where location_id = %s", AddressDto, location_id)

    async def delete_location_by_id(self, location_id: int) -> int:
        return await self.db.update("delete from address where location_id = %s", location_id)
