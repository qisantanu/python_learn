from sqlmodel import SQLModel, Field
from typing import List, Optional

class Item(SQLModel, table=True):
    __tablename__ = "items"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str = None
    price: float
    tax: float = None

### CREATE SCHEMAs ###

class ItemRead(SQLModel):
    id: int
    name: str
    description: str = None
    price: float

class Pagination(SQLModel):
    items: List[ItemRead]
    total: int
    page: int
    page_size: int

class ItemCreate(SQLModel):
    name: str
    description: str = None
    price: float
    tax: float

class ItemUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: Optional[float] = None
