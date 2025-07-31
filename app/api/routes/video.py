from fastapi import APIRouter

router = APIRouter(prefix="/video", tags=["Video"])


@router.get("/")
async def generate():
    """Generate video"""
    return {"message": "Video generated"} 