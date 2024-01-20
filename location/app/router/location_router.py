from fastapi import APIRouter
from app.controller.location_controller import LocationController
from app.model.address import Address


class LocationRouter:

    def __init__(self, location_controller: LocationController):
        self.location_controller = location_controller
        self.router = APIRouter(
            prefix="/location",
            tags=["location"]
        )
        self.router.add_api_route(
            path="/{location_id}",
            summary="Gets the data associated with a location_id",
            endpoint=self.get_location_by_id,
            methods=["GET"],
            response_description="Get location level data associated with location_id"
        )
        self.router.add_api_route(
            path="/{location_id}",
            summary="Delete a location associated with a location_id",
            endpoint=self.delete_location_by_id,
            methods=["DELETE"],
            response_description="Deletes a location by location_id"
        )

    async def get_location_by_id(self, location_id) -> Address:
        return await self.location_controller.get_location_by_id(location_id)

    async def delete_location_by_id(self, location_id) -> bool:
        rows_update = await self.location_controller.delete_location_by_id(location_id)
        if rows_update == 1:
            return True
        else:
            return False
