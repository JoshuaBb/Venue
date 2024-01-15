
from fastapi import APIRouter
from app.controller.location_controller import LocationController

class LocationRouter():

    def __init__(self, location_controller: LocationController):
        self.location_controller = location_controller
        self.router = APIRouter(
            prefix="/location"
        )
        self.router.add_api_route(
            path="/{location_id}",
            endpoint=self.location_controller.get_location_by_id,
            methods=["GET"]
        )


