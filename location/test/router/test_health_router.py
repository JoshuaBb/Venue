import unittest
from fastapi.testclient import TestClient
from app.router import health

class SumTest(unittest.TestCase):
    client = TestClient(health.router)

    def test_health(self):
        response = self.client.get("/health")
        assert response.status_code == 200

