from sqlmodel import SQLModel, Field
from typing import List, Optional
from pydantic import BaseModel

class UserRole(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str

### CREATE SCHEMAs ###
