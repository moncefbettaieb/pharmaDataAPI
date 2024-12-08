from fastapi import APIRouter
from app.api.v1.endpoints import users, products, auth, subscription

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(subscription.router, prefix="/subscription", tags=["subscription"])