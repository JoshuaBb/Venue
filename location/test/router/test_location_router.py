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
        location_id = 1
        address = Address()
        address.location_id = location_id
        location_controller.get_location_by_id.return_value = address
        location_router = LocationRouter(location_controller)
        async with AsyncClient(app=location_router.router, base_url="http://test") as ac:
            response = await ac.get(f"/location/{location_id}")
        assert response.status_code == 200
        assert response.json().get('location_id') == address.location_id
