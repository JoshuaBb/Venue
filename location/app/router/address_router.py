from fastapi import APIRouter
from app.controller.address_controller import AddressController
from app.model.address import Address


class AddressRouter:

    def __init__(self, address_controller: AddressController):
        self.address_controller = address_controller
        self.router = APIRouter(
            prefix="/address",
            tags=["Address"]
        )
        self.router.add_api_route(
            path="/{address_id}",
            summary="Gets the data associated with a address_id",
            endpoint=self.get_address_by_id,
            methods=["GET"],
            response_description="Get address level data associated with address_id"
        )
        self.router.add_api_route(
            path="/{address_id}",
            summary="Delete an address associated with a address_id",
            endpoint=self.delete_address_by_id,
            methods=["DELETE"],
            response_description="Deletes an address by address_id"
        )

    async def get_address_by_id(self, address_id) -> Address:
        """API handler for getting address data by address_id"""
        return await self.address_controller.get_address_by_id(address_id)

    async def delete_address_by_id(self, address_id) -> bool:
        """API handler for deleting address data using the address_id"""
        rows_update = await self.address_controller.delete_address_by_id(address_id)
        if rows_update == 1:
            return True
        else:
            return False
