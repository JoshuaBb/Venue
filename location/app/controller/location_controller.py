from app.model.address import Address, from_dto
from app.util.redis_manager import RedisManager
from app.store.location_store import LocationStore


class LocationController():

    def __init__(self, redis_manager: RedisManager, location_store: LocationStore):
        self.location_store = location_store
        self.redis_manager = redis_manager

    async def get_location_by_id(self, location_id: int):
        location_str = await self.redis_manager.get(location_id)
        if location_str is None:
            location_dto = await self.location_store.get_location_by_id(location_id)
            # Stubbed for now
            if location_dto is None:
                location = Address(location_id=location_id, latitude=2.0, longitude=3.0)
                return location
            else:
                location = from_dto(location_dto)
                await self.redis_manager.set(str(location_id), str(location.model_dump_json()))
                return from_dto(location_dto)
        else:
            location = Address.parse_raw(location_str)
        return location

    async def delete_location_by_id(self, location_id) -> int:
        row_count = await self.location_store.delete_location_by_id(location_id)
        if row_count == 1:
            await self.redis_manager.delete(location_id)
        return row_count
