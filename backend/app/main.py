from fastapi import FastAPI
from app.rag.services.database import engine, Base
import app.rag.models.document
from app.api.routes.research import router as research_router
from app.api.routes.upload import router as upload_router
from app.api.routes.rag import router as rag_router

app = FastAPI(
    title="AI Research Assistant API",
    version="1.0.0",
)

app.include_router(upload_router)
app.include_router(rag_router)


@app.get("/")
def root():
    return {"message": "API is running"}


Base.metadata.create_all(bind=engine)


app.include_router(
    research_router,
    prefix="/api",
    tags=["Research"],
)
