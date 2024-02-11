# main.py

from fastapi import FastAPI
from app.api import order  # Import the order router

app = FastAPI()

# Include the order router
app.include_router(order.router, prefix="/api")
