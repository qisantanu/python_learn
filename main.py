from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel
from database.database import engine
from controllers.items import router as items_router

# Create FastAPI instance
app = FastAPI()
app.include_router(items_router)

# # Root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}

#     return {"item_id": item_id, "q": q}

# to run the FastAPI app, use the command:
# uvicorn main:app --reload
    

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
