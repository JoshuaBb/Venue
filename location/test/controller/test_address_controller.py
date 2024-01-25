import unittest
import pytest
import asyncio
from unittest.mock import patch
from app.util.redis_manager import RedisManager
from app.dto.address_dto import AddressDto
from app.store.address_store import AddressStore
from app.model.address import CreateAddressRequest, AddressResponse, to_address, from_dto
from app.util.google_maps_manager import GoogleMapsManager, GoogleMapsInfo
from app.controller.address_controller import AddressController
from app.router.address_router import CreateAddressRequest
from mockito import when


class AddressControllerTest(unittest.IsolatedAsyncioTestCase):

    @patch('app.util.redis_manager.RedisManager')
    @patch('app.store.address_store.AddressStore')
    @patch('app.util.google_maps_manager.GoogleMapsManager')
    @pytest.mark.asyncio
    async def test_delete_address_by_id(self, redis_manager: RedisManager, address_store: AddressStore,
                                        google_maps_manager: GoogleMapsManager):
        impl = AddressController(redis_manager, address_store, google_maps_manager)
        address_id = 2

        row_count = asyncio.Future()
        row_count.set_result(1)
        when(address_store).delete_address_by_id(address_id).thenReturn(row_count)

        delete = asyncio.Future()
        delete.set_result("N/A")
        when(redis_manager).delete(address_id).thenReturn(delete)

        result = await impl.delete_address_by_id(address_id)

        assert result == 1

    @patch('app.util.redis_manager.RedisManager')
    @patch('app.store.address_store.AddressStore')
    @patch('app.util.google_maps_manager.GoogleMapsManager')
    @pytest.mark.asyncio
    async def test_post_address(self, redis_manager: RedisManager, address_store: AddressStore,
                                google_maps_manager: GoogleMapsManager):
        impl = AddressController(redis_manager, address_store, google_maps_manager)
        create_address = CreateAddressRequest(
            address_line_one="Some Street address",
            city="Denver",
            state_or_province="CO",
            zip_or_postal="80234",
            country_code="US",
            latitude=1.0,
            longitude=1.0
        )
        google_maps_info = GoogleMapsInfo("place_id_value")

        g_map_info = asyncio.Future()
        g_map_info.set_result(google_maps_info)

        when(google_maps_manager).get_google_maps_info(create_address.address(), create_address.city,
                                                       create_address.state_or_province, create_address.latitude,
                                                       create_address.longitude).thenReturn(g_map_info)

        address = to_address(create_address, google_maps_info)

        row_count = asyncio.Future()
        row_count.set_result(1)

        when(address_store).insert_address(address).thenReturn(row_count)

        result = await impl.post_address(create_address)
        assert result == 1

    @patch('app.util.redis_manager.RedisManager')
    @patch('app.store.address_store.AddressStore')
    @patch('app.util.google_maps_manager.GoogleMapsManager')
    @pytest.mark.asyncio
    async def test_find_addresses(self, redis_manager: RedisManager, address_store: AddressStore,
                                  google_maps_manager: GoogleMapsManager):
        impl = AddressController(redis_manager, address_store, google_maps_manager)
        address = AddressResponse(address_id=1)

        address_result = asyncio.Future()
        address_result.set_result([address])

        when(address_store).find_addresses().thenReturn(address_result)

        result = await impl.find_addresses()
        assert result == [from_dto(address)]

    @patch('app.util.redis_manager.RedisManager')
    @patch('app.store.address_store.AddressStore')
    @patch('app.util.google_maps_manager.GoogleMapsManager')
    @pytest.mark.asyncio
    async def test_get_address_by_id_with_cache(self, redis_manager: RedisManager, address_store: AddressStore,
                                                google_maps_manager: GoogleMapsManager):
        impl = AddressController(redis_manager, address_store, google_maps_manager)
        address_id = 1
        address = AddressResponse()
        address.address_id = address_id

        address_result = asyncio.Future()
        address_result.set_result(address.json())

        when(redis_manager).get(address_id).thenReturn(address_result)

        result = await impl.get_address_by_id(address_id)
        assert result == address

    @patch('app.util.redis_manager.RedisManager')
    @patch('app.store.address_store.AddressStore')
    @patch('app.util.google_maps_manager.GoogleMapsManager')
    @pytest.mark.asyncio
    async def test_get_address_by_id_without_cache(self, redis_manager: RedisManager, address_store: AddressStore,
                                                   google_maps_manager: GoogleMapsManager):
        impl = AddressController(redis_manager, address_store, google_maps_manager)
        address_id = 1
        address = AddressDto()
        address.address_id = address_id
        address.address_line_one = "Some Address"
        address.city = "Denver"
        address.state_or_province = "CO"
        address.zip_or_postal = "34323"
        address.country_code = "US"
        address.latitude = 1.0
        address.longitude = 1.0
        address.place_id = "Some_Place_Id"

        address_cache_result = asyncio.Future()
        address_cache_result.set_result(None)

        when(redis_manager).get(address_id).thenReturn(address_cache_result)

        address_result = asyncio.Future()
        address_result.set_result(address)

        when(address_store).get_address_by_id(address_id).thenReturn(address_result)
        when(redis_manager).set(str(address_id), from_dto(address).json()).thenReturn(address_cache_result)

        result = await impl.get_address_by_id(address_id)
        assert result == from_dto(address)
