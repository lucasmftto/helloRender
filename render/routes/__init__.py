from fastapi import APIRouter

from .notification import router as notification_route

main_router = APIRouter()


main_router.include_router(notification_route, prefix="/notification", tags=["notification"])

