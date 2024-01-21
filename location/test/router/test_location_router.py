import unittest
from app.controller.location_controller import LocationController
from app.router.location_router import LocationRouter
from app.model.address import Address
from unittest.mock import patch
import pytest
from httpx import AsyncClient


class HealthRouterTest(unittest.IsolatedAsyncioTestCase):

    @patch('app.controller.location_controller.LocationController')
    @pytest.mark.asyncio
    async def test_get_location(self, location_controller: LocationController):
        address_id = 1
        address = Address()
        address.address_id = address_id
        location_controller.get_address_by_id.return_value = address
        location_router = LocationRouter(location_controller)
        async with AsyncClient(app=location_router.router, base_url="http://test") as ac:
            response = await ac.get(f"/location/{address_id}")
        assert response.status_code == 200
        assert response.json().get('address_id') == address.address_id
