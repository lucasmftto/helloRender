from fastapi import APIRouter, Body, BackgroundTasks, Depends
from render.auth import get_current_active_user
from render.models import User

router = APIRouter()


@router.get('/')
async def root(current_user: User = Depends(get_current_active_user)):
    return {"message": "Hello Bruno! Send me a notification!"}
