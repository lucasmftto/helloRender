import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .routes import main_router
from db import AsyncIOMotorClient, get_database


app = FastAPI(
    title="hello-bruno-api",
    version="0.1.0",
    description="test render",
)

app.include_router(main_router)


@app.get('/')
async def root(mongo_db: AsyncIOMotorClient = Depends(get_database)):
    actins_collection = mongo_db["render"]["actions"]
    await actins_collection.insert_one({"action": "GET /"})
    rows = actins_collection.find({}, {'_id': 0})
    actions = await rows.to_list(length=1000)
    return JSONResponse(jsonable_encoder(actions))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)