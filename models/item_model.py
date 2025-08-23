from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from pydantic import field_validator

class Item(SQLModel, table=True):
    __tablename__ = "items"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str = None
    price: float
    tax: float = None
    # Foreign key
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")

    # belongs_to user
    user: Optional["User"] = Relationship(back_populates="items")

    # custom validation
    @field_validator('price')
    def validate_price(cls, value):
        if (value < 0):
            raise ValueError('Price must be positive')
        return value;

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
