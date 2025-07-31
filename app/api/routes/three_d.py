from fastapi import APIRouter

router = APIRouter(prefix="/3d", tags=["3D"])


@router.get("/")
async def generate():
    """Generate 3D model"""
    return {"message": "3D model generated"} 