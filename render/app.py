import uvicorn
from fastapi import FastAPI
from routes import main_router

app = FastAPI(
    title="hello-bruno-api",
    version="0.1.0",
    description="test render",
)

app.include_router(main_router)


@app.get('/')
async def root():
    return {"message": "Hello Bruno!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)