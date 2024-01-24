import unittest
import pytest
import asyncio
from unittest.mock import patch
from app.util.redis_manager import RedisManager
from app.store.address_store import AddressStore
from app.util.google_maps_manager import GoogleMapsManager
from app.controller.address_controller import AddressController


class AddressControllerTest(unittest.IsolatedAsyncioTestCase):

    @patch('app.util.redis_manager.RedisManager')
    @patch('app.store.address_store.AddressStore')
    @patch('app.util.google_maps_manager.GoogleMapsManager')
    @pytest.mark.asyncio
    async def test_delete_address_by_id(self, redis_manager: RedisManager, address_store: AddressStore,
                                        google_maps_manager: GoogleMapsManager):
        address_controller = AddressController(redis_manager, address_store, google_maps_manager)

        address_id = 2

        row_count = asyncio.Future()
        row_count.set_result(1)
        address_store.delete_address_by_id.return_value = row_count

        delete = asyncio.Future()
        delete.set_result("N/A")
        redis_manager.delete.return_value = delete

        result = await address_controller.delete_address_by_id(address_id)

        assert result == 1
