"""Module created to handle Health Checks"""
from fastapi import APIRouter

class HealthRouter:
    """HealthRouter Class handles health checks"""

    def __init__(self):
        self.router = APIRouter(
            prefix="/health",
            tags=["health"]
        )
        self.router.add_api_route(
            path="/",
            summary="Simple health check endpoint",
            endpoint=self.get_health_check,
            methods=["GET"],
            response_description="""Returns a 200 response with a message indicating
             that the service is running"""
        )

    def get_health_check(self):
        """Health check endpoint to verify that the service is running.

        Returns:
            dict: A dictionary containing the status and message.
        """
        return {"status": "UP", "message": "Everything WORKS!"}
