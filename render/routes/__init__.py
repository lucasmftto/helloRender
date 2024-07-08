from fastapi import APIRouter

from .notification import router as notification_route
from .auth import router as auth_router

main_router = APIRouter()


main_router.include_router(notification_route, prefix="/notification", tags=["notification"])
main_router.include_router(auth_router, tags=["auth"])

