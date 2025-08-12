from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Optional
from models.item_model import Item, ItemRead, Pagination, ItemCreate, ItemUpdate
from sqlmodel import Session, select, or_
from database.database import engine

router = APIRouter()

### CRUD operations using FastAPI ###
# INDEX
@router.get("/items/", response_model=Pagination)
def get_items(min_price: Optional[float] = None, 
              max_price: Optional[float] = None, 
              search: Optional[str] = None,
              page: int = 1,
              page_size: int = 10):
    with Session(engine) as session:
        query = select(Item)

        if min_price is not None:
            query = query.where(Item.price >= min_price)

        if max_price is not None:
            query = query.where(Item.price <= max_price)

        if search is not None:
            query = query.where(or_(Item.name.contains(search), Item.description.contains(search)))
            
        if page_size is not None:
            query = query.offset((page - 1) * page_size).limit(page_size)
        else:
            query = query.limit(100)

        items = session.exec(query).all()
        
        pagianted_items = Pagination(items=items, total=len(items), page=page, page_size=page_size)
        return pagianted_items
    
# SHOW
@router.get("/items/{item_id}", response_model=ItemRead)
def get_item(item_id: int):
  with Session(engine) as session:    
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

# CREATE
@router.post("/items/", response_model=Item)
def create_item(item: ItemCreate):
    db_item = Item(**item.dict())
    with Session(engine) as session:
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

# UPDATE
@router.put("/items/{item_id}", response_model=ItemUpdate)
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
@router.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)

        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        session.delete(item)
        session.commit()
        return { 'message': "Item deleted successfully" }