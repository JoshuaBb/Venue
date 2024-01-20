from app.model.address import Address, from_dto
from app.util.redis_manager import RedisManager
from app.store.address_store import AddressStore


class AddressController():

    def __init__(self, redis_manager: RedisManager, address_store: AddressStore):
        self.address_store = address_store
        self.redis_manager = redis_manager

    async def get_address_by_id(self, address_id: int):
        """Gets a address by a address_id.
        It will first look in Redis Cache and then query the database if it is missing
        """
        address_str = await self.redis_manager.get(address_id)
        if address_str is None:
            address_dto = await self.address_store.get_address_by_id(address_id)
            # Stubbed for now
            if address_dto is None:
                location = Address(location_id=address_id, latitude=2.0, longitude=3.0)
                return location
            else:
                location = from_dto(address_dto)
                await self.redis_manager.set(str(address_id), str(location.model_dump_json()))
                return from_dto(address_dto)
        else:
            location = Address.parse_raw(address_str)
        return location

    async def delete_address_by_id(self, address_id) -> int:
        """Deletes a address by address_id. It will also remove the location data from the Redis Cache"""
        row_count = await self.address_store.delete_address_by_id(address_id)
        if row_count == 1:
            await self.redis_manager.delete(address_id)
        return row_count
