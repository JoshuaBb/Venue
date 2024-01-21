from app.controller import address_controller
from app.util.redis_manager import RedisManager
from app.util.google_maps_manager import GoogleMapsManager
from app.router import address_router, health_router
from app.util.database import Db
from app.store import address_store
import datetime
import logging

logging.basicConfig(level=logging.INFO, filemode='w', format=f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - %(levelname)s - %(message)s')

db_connection = Db()

# Redis
redis_manager = RedisManager("address")

# Google Maps
google_maps_manager = GoogleMapsManager()

# Store
location_store = address_store.AddressStore(db_connection)

# Controllers
location_controller = address_controller.AddressController(redis_manager, location_store, google_maps_manager)

# Routers
health_router = health_router.HealthRouter()
address_router = address_router.AddressRouter(location_controller)

routers = [health_router.router, address_router.router]