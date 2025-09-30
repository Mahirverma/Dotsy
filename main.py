from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.models import users, knowledge_base, document

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def read_root():
    return {"msg": "Knowledge Base API is running"}