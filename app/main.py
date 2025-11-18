from fastapi import FastAPI
from app.routes.face_recognition import router as face_router

app = FastAPI(title="AWS Face Recognition Service")
app.include_router(face_router, prefix="/face")