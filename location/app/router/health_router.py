from fastapi import APIRouter
class HealthRouter():

    def __init__(self):
        self.router = APIRouter(
            prefix="/health"
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.get_health,
            methods=["GET"]
        )

    def get_health(self):
        return "Everything WORKS!"

