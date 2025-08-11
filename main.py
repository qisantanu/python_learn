from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Field, create_engine, Session, select, SQLModel, or_

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

### Create SCHEMAs

class ItemCreate(SQLModel):
    name: str
    description: str = None
    price: float
    tax: float

class ItemRead(SQLModel):
    id: int
    name: str
    description: str = None
    price: float

class ItemUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: Optional[float] = None
    

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
@app.get("/items/", response_model=List[ItemRead])
def get_items(min_price: Optional[float] = None, max_price: Optional[float] = None, search: Optional[str] = None):
    with Session(engine) as session:
        query = select(Item)

        if min_price is not None:
            query = query.where(Item.price >= min_price)

        if max_price is not None:
            query = query.where(Item.price <= max_price)

        if search is not None:
            query = query.where(or_(Item.name.contains(search), Item.description.contains(search)))
            

        items = session.exec(query).all()
        return items

# SHOW
@app.get("/items/{item_id}", response_model=ItemRead)
def get_item(item_id: int):
  with Session(engine) as session:    
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

# CREATE
@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate):
    db_item = Item(**item.dict())
    with Session(engine) as session:
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

# UPDATE
@app.put("/items/{item_id}", response_model=ItemUpdate)
def update_item(item_id: int, item_to_update: ItemUpdate):
    with Session(engine) as session:
        item  = session.get(Item, item_id)

        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        updated_item = item_to_update.dict(exclude_unset=True)

        if not updated_item:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        for key, value in updated_item.items():
            setattr(item, key, value)

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