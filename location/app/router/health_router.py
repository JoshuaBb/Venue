from fastapi import APIRouter
class HealthRouter():

    def __init__(self):
        self.router = APIRouter(
            prefix="/health",
            tags=["health"]
        )
        self.router.add_api_route(
            path="/",
            summary="Simple health check endpoint",
            endpoint=self.get_health,
            methods=["GET"],
            response_description="Gets a 200 response a message indicate that the service is running"
        )

    def get_health(self):
        return "Everything WORKS!"

