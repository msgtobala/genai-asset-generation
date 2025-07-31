from .user import router as user_router
from .image import router as image_router
from .video import router as video_router
from .three_d import router as three_d_router

__all__ = ["user_router", "image_router", "video_router", "three_d_router"]