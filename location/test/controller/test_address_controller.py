import unittest
import pytest
import asyncio
from unittest.mock import patch
from app.util.redis_manager import RedisManager
from app.store.address_store import AddressStore
from app.model.address import CreateAddressRequest, to_address
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

        when(google_maps_manager).get_google_maps_info(create_address.address(), create_address.city, create_address.state_or_province, create_address.latitude, create_address.longitude).thenReturn(g_map_info)

        address = to_address(create_address, google_maps_info)

        row_count = asyncio.Future()
        row_count.set_result(1)

        when(address_store).insert_address(address).thenReturn(row_count)

        result = await impl.post_address(create_address)
        assert result == 1






