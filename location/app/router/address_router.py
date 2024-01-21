from fastapi import APIRouter
from app.controller.address_controller import AddressController
from app.model.address import Address, CreateAddress
from typing import Optional


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
            response_model=Address,
            response_description="Get address level data associated with address_id"
        )
        self.router.add_api_route(
            path="/{address_id}",
            summary="Delete an address associated with a address_id",
            endpoint=self.delete_address_by_id,
            methods=["DELETE"],
            response_description="Deletes an address by address_id"
        )
        # Not yet able to handle duplicates
        self.router.add_api_route(
            path="/",
            summary="Inserts address data into the database",
            endpoint=self.post_address,
            response_description="Inserts address data",
            methods=["POST"],
        )

    async def get_address_by_id(self, address_id) -> Optional[Address]:
        """API handler for getting address data by address_id"""
        return await self.address_controller.get_address_by_id(address_id)

    async def post_address(self, address: CreateAddress) -> int:
        """API handler for insert address level data"""
        return await self.address_controller.post_address(address)

    async def delete_address_by_id(self, address_id) -> bool:
        """API handler for deleting address data using the address_id"""
        rows_update = await self.address_controller.delete_address_by_id(address_id)
        if rows_update == 1:
            return True
        else:
            return False
