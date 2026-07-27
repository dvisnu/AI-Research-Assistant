from fastapi import FastAPI
from app.database.sqlite import engine, Base
from app.database import models
from app.api.upload import router as upload_router

app = FastAPI(
    title="AI Research Assistant API",
    version="1.0.0",
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {"message": "API is running"}



Base.metadata.create_all(bind=engine)