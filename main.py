from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Field, create_engine, declarative_base, Session, Select, func

# Create FastAPI instance
app = FastAPI()

# # Root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}

# # Example endpoint with path parameter
# # http://127.0.0.1:8000/items/1?q=hello
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# to run the FastAPI app, use the command:
# uvicorn main:app --reload

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# simulating a database with a list
fake_db = []

# INDEX
@app.get("/items/", response_model=List[Item])
def get_items():
    return fake_db

# SHOW
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
  if item_id >= len(fake_db) or item_id < 0:
    raise HTTPException(status_code=404, detail="Item not found")
  
  return fake_db[item_id]

# CREATE
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    fake_db.append(item)
    return item

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id >= len(fake_db) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")

    fake_db[item_id] = item
    return item

# DELETE
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    if item_id >= len(fake_db) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
     
    del fake_db[item_id]
    return {"message": "Item deleted successfully"}