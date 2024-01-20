from fastapi import FastAPI
from app.router import location_router, health_router
from app.controller import location_controller
from app.util.redis_manager import RedisManager
from app.util.google_maps_manager import GoogleMapsManager
from app.util.database import Db
from app.store import location_store
import datetime
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO, filemode='w', format=f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - %(levelname)s - %(message)s')

# Postgres Connection (TODO make environmental variable)
db_connection = Db()

# Redis
redis_manager = RedisManager(host="redis", port=6379)

# Google Maps
google_maps_manager = GoogleMapsManager()

# Store
location_store = location_store.LocationStore(db_connection)

# Controllers
location_controller = location_controller.LocationController(redis_manager, location_store)

# Routers
health_router = health_router.HealthRouter()
location_router = location_router.LocationRouter(location_controller)

# Adding Routes
app.include_router(location_router.router)
app.include_router(health_router.router)
