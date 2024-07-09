import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from render.config import settings
from fastapi import Depends

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
db = client.get_default_database(settings.mongodb_db)
users_collection = db.get_collection("users")


async def get_database() -> AsyncIOMotorClient:
    return db.client

ActiveSession = Depends(get_database)


async def get_user_collection():
    return users_collection

ActiveSession = Depends(get_user_collection)
