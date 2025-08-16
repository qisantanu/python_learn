from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from pydantic import BaseModel
import enum
from models.item_model import Item # careful with circular import


class UserRole(str, enum.Enum):
    admin = "admin"
    user = "XXXX"
    guest = "guest"
    
class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
    user_role: UserRole = Field(default=UserRole.user)
    adhar_no: Optional[str] = None

    # has many
    items: List["Item"] = Relationship(back_populates="user")

### CREATE SCHEMAs ###

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserRead(BaseModel):
    id: int
    username: str
    user_role: UserRole
    adhar_no: Optional[str] = None

class UserUpdate(BaseModel):
    adhar_no: Optional[str] = None
    user_role: UserRole = Field(default=UserRole.user)