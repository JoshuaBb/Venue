import unittest
from app.controller.address_controller import AddressController
from app.router.address_router import AddressRouter
from app.model.address import AddressResponse
from unittest.mock import patch
import pytest
from httpx import AsyncClient


class AddressRouterTest(unittest.IsolatedAsyncioTestCase):

    @patch('app.controller.address_controller.AddressController')
    @pytest.mark.asyncio
    async def test_get_address_by_id(self, address_controller: AddressController):
        address_id = 1
        address = AddressResponse()
        address.address_id = address_id
        address_controller.get_address_by_id.return_value = address
        address_router = AddressRouter(address_controller)
        async with AsyncClient(app=address_router.router, base_url="http://test") as ac:
            response = await ac.get(f"/address/{address_id}")
        assert response.status_code == 200
        assert response.json().get('address_id') == address.address_id

    @patch('app.controller.address_controller.AddressController')
    @pytest.mark.asyncio
    async def test_find_addresses(self, address_controller: AddressController):
        address_id = 1
        address = AddressResponse()
        address.address_id = address_id
        address_controller.find_addresses.return_value = [address]
        address_router = AddressRouter(address_controller)
        async with AsyncClient(app=address_router.router, base_url="http://test") as ac:
            response = await ac.get(f"/address/")
        assert response.status_code == 200
        assert response.json()[0].get('address_id') == address.address_id
