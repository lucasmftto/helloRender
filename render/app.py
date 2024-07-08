import uvicorn
from fastapi import FastAPI, Depends, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from render.models import User
from render.routes import main_router
from render.db import AsyncIOMotorClient, get_database
from render.auth import get_user

app = FastAPI(
    title="hello-bruno-api",
    version="0.1.0",
    description="test render",
)

app.include_router(main_router)


@app.get('/')
async def root(mongo_db: AsyncIOMotorClient = Depends(get_database)):
    user_collection = mongo_db["render"]["users"]
    user = await get_user("lucas", user_collection)

    return JSONResponse(jsonable_encoder(user))


@app.post(
    "/",
    response_description="Add new user",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_user(user: User = Body(...),
                      mongo_db: AsyncIOMotorClient = Depends(get_database)):
    """
    Insert a new user.

    A unique `id` will be created and provided in the response.
    """
    actions_collection = mongo_db["render"]["users"]
    new_user = await actions_collection.insert_one(
        user.model_dump(by_alias=True, exclude=["id"])
    )
    created_student = await actions_collection.find_one(
        {"_id": new_user.inserted_id}
    )
    return created_student


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
