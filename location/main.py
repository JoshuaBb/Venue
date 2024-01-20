from fastapi import FastAPI
from app.global_context import routers

app = FastAPI()

# Adding Routes
for router in routers:
    app.include_router(router)
    app.include_router(router)
