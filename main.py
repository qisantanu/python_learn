from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from sqlmodel import SQLModel
from database.database import engine
from controllers.items import router as items_router
from controllers.users import router as users_router

# Create FastAPI instance
app = FastAPI()
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(items_router)
app.include_router(users_router)

# # Root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}

#     return {"item_id": item_id, "q": q}

# to run the FastAPI app, use the command:
# uvicorn main:app --reload --log-config=log_conf.yml
    

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
