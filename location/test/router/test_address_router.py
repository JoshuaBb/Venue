import unittest
from app.controller.address_controller import AddressController
from app.router.address_router import AddressRouter
from app.model.address import AddressResponse, CreateAddressRequest
from unittest.mock import patch
import pytest
from httpx import AsyncClient
import asyncio


class AddressRouterTest(unittest.IsolatedAsyncioTestCase):

    @patch('app.controller.address_controller.AddressController')
    @pytest.mark.asyncio
    async def test_get_address_by_id(self, address_controller: AddressController):
        address_id = 1
        address = AddressResponse()
        address.address_id = address_id
        awaitable = asyncio.Future()
        awaitable.set_result(address)
        address_controller.get_address_by_id.return_value = awaitable
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
        awaitable = asyncio.Future()
        awaitable.set_result([address])
        address_controller.find_addresses.return_value = awaitable
        address_router = AddressRouter(address_controller)
        async with AsyncClient(app=address_router.router, base_url="http://test") as ac:
            response = await ac.get(f"/address/")
        assert response.status_code == 200
        assert response.json()[0].get('address_id') == address.address_id

    @patch('app.controller.address_controller.AddressController')
    @pytest.mark.asyncio
    async def test_delete_address_by_id(self, address_controller: AddressController):
        awaitable = asyncio.Future()
        awaitable.set_result(1)
        address_controller.delete_address_by_id.return_value = awaitable
        address_router = AddressRouter(address_controller)
        async with AsyncClient(app=address_router.router, base_url="http://test") as ac:
            response = await ac.delete(f"/address/1")
        assert response.status_code == 200

    @patch('app.controller.address_controller.AddressController')
    @pytest.mark.asyncio
    async def test_post_address(self, address_controller: AddressController):
        address = CreateAddressRequest(
            address_line_one="Some Street address",
            city = "Denver",
            state_or_province="CO",
            zip_or_postal="80234",
            country_code="US",
            latitude=1.0,
            longitude=1.0
        )
        awaitable = asyncio.Future()
        awaitable.set_result(1)

        address_controller.post_address.return_value = awaitable

        address_router = AddressRouter(address_controller)
        async with AsyncClient(app=address_router.router, base_url="http://test") as ac:
            response = await ac.post(f"/address/", content=address.json())
        assert response.status_code == 200
