from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Field, create_engine, Session, select, SQLModel

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

class Item(SQLModel, table=True):
    __tablename__ = "items"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str = None
    price: float
    tax: float = None

# simulating a database with a list
fake_db = []

#### database connection ####
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

### CRUD operations using FastAPI ###

# INDEX
@app.get("/items/", response_model=List[Item])
def get_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items

# SHOW
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
  with Session(engine) as session:    
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

# CREATE
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    with Session(engine) as session:
        item  = session.get(Item, item_id)

        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        item.name = updated_item.name
        item.description = updated_item.description
        item.price = updated_item.price
        item.tax = updated_item.tax
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

# DELETE
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)

        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        session.delete(item)
        session.commit()
        return { 'message': "Item deleted successfully" }