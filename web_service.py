import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="hello-bruno-api",
    version="0.1.0",
    description="test render",
)


@app.get('/')
async def root():
    return {"message": "Hello Bruno!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)