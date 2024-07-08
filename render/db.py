import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from render.config import settings
from fastapi import Depends

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
db = client.get_default_database(settings.mongodb_db)
actins_collection = db.get_collection("actions")


async def get_database() -> AsyncIOMotorClient:
    return db.client


ActiveSession = Depends(get_database)
