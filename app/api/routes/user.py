from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/")
async def get():
    """Get user"""
    return {"message": "User"} 