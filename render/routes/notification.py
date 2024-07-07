from fastapi import APIRouter, Body, BackgroundTasks

router = APIRouter()


@router.get('/')
async def root():
    return {"message": "Hello Bruno! Send me a notification!"}