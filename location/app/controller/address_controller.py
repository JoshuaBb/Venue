from app.model.address import AddressResponse, from_dto, to_address, CreateAddressRequest
from app.util.redis_manager import RedisManager
from app.store.address_store import AddressStore
from app.util.google_maps_manager import GoogleMapsManager
from typing import Optional


class AddressController():

    def __init__(self, redis_manager: RedisManager, address_store: AddressStore,
                 google_maps_manager: GoogleMapsManager):
        self.address_store = address_store
        self.redis_manager = redis_manager
        self.google_maps_manager = google_maps_manager

    async def get_address_by_id(self, address_id: int) -> Optional[AddressResponse]:
        """Gets a address by a address_id.
        It will first look in Redis Cache and then query the database if it is missing
        """
        address_str = await self.redis_manager.get(address_id)
        if address_str is None:
            address_dto = await self.address_store.get_address_by_id(address_id)
            # Stubbed for now
            if address_dto:
                location = from_dto(address_dto)
                await self.redis_manager.set(str(address_id), str(location.json()))
                return from_dto(address_dto)
            return None
        else:
            location = AddressResponse.parse_raw(address_str)
            return location

    async def delete_address_by_id(self, address_id) -> int:
        """Deletes a address by address_id. It will also remove the location data from the Redis Cache"""
        row_count = await self.address_store.delete_address_by_id(address_id)
        if row_count == 1:
            await self.redis_manager.delete(address_id)
        return row_count

    async def post_address(self, address: CreateAddressRequest) -> int:
        """Using the Google Maps API, it will retrieve lat and lon and persist the location data into the database"""
        google_maps_info = await self.google_maps_manager.get_google_maps_info(address.address(), address.city, address.state_or_province, address.latitude, address.longitude)
        if google_maps_info:
            return await self.address_store.insert_address(to_address(address, google_maps_info))
        else:
            # TODO make better
            return 0

    async def find_addresses(self) -> list[AddressResponse]:
        address_dtos = await self.address_store.find_addresses()
        if address_dtos:
            result = [from_dto(x) for x in address_dtos]
            return result
        else:
            return []

