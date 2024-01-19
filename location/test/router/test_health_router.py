import unittest
from fastapi.testclient import TestClient
from app.router.health_router import HealthRouter

class SumTest(unittest.TestCase):
    client = TestClient(HealthRouter().router)

    def test_health(self):
        response = self.client.get("/health")
        assert response.status_code == 200

