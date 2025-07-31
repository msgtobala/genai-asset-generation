from fastapi import APIRouter

router = APIRouter(prefix="/image", tags=["Image"])


@router.get("/")
async def generate():
    """Generate image"""
    return {"message": "Image generated"} 