from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

from app.api.routes import user_router
from app.api.routes import three_d_router
from app.api.routes import image_router
from app.api.routes import video_router

load_dotenv()

app = FastAPI(title="Concert backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(image_router)
app.include_router(video_router)
app.include_router(three_d_router)

@app.get("/")
def root():
    return {"message": "Concert backend is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
