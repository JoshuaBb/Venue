from fastapi import APIRouter, HTTPException
from app.controller.address_controller import AddressController
from app.model.address import AddressResponse, CreateAddressRequest
from typing import Optional, List

class AddressRouter:

    def __init__(self, address_controller: AddressController):
        self.address_controller = address_controller
        self.router = APIRouter(
            prefix="/address",
            tags=["Address"]
        )
        self.router.add_api_route(
            path="/{address_id}",
            summary="Gets the data associated with an address_id",
            endpoint=self.get_address_by_id,
            methods=["GET"],
            response_model=AddressResponse,
            response_description="Get address level data associated with an address_id"
        )
        self.router.add_api_route(
            path="/{address_id}",
            summary="Delete an address associated with an address_id",
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
        self.router.add_api_route(
            path="/",
            summary="Gets all addresses currently in the database",
            endpoint=self.find_addresses,
            response_description="Gets all address data",
            methods=["GET"],
        )

    async def get_address_by_id(self, address_id) -> Optional[AddressResponse]:
        """API handler for getting address data by address_id"""
        try:
            return await self.address_controller.get_address_by_id(address_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def post_address(self, address: CreateAddressRequest) -> int:
        """API handler for inserting address level data"""
        try:
            return await self.address_controller.post_address(address)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def delete_address_by_id(self, address_id) -> None:
        """API handler for deleting address data using the address_id"""
        try:
            rows_updated = await self.address_controller.delete_address_by_id(address_id)
            if rows_updated == 0:
                raise HTTPException(status_code=404, detail=f"Address with id {address_id} not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def find_addresses(self) -> List[AddressResponse]:
        """API handler for getting all addresses"""
        try:
            return await self.address_controller.find_addresses()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))