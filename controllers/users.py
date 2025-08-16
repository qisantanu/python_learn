from fastapi import HTTPException, APIRouter, Depends
from pydantic import BaseModel
from typing import List, Optional
from models.user_model import User, UserCreate, UserLogin, Token, UserRead, UserUpdate
from helpers.password_hashing import hash_password, verify_password
from helpers.json_wt import create_access_token
from sqlmodel import Session, select
from database.database import engine
from helpers.current_user import get_current_user

router = APIRouter()

### CRUD operations using FastAPI ###
# CREATE
@router.post("/signup", response_model=Token, tags=["users"])
def signup(user: UserCreate, session: Session = Depends(lambda: Session(engine))):
    with Session(engine) as session:
        query = select(User)
        # Check if the username already exists
        db_user = session.exec(query.where(User.username == user.username)).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        hashed_pwd = hash_password(user.password)
        new_user = User(username=user.username, hashed_password=hashed_pwd)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        token = create_access_token({"sub": new_user.username})
        return Token(access_token=token, token_type="bearer")

@router.post("/login", response_model=Token, tags=["users"])
def login(user: UserLogin, session: Session = Depends(lambda: Session(engine))):
    with Session(engine) as session:
        find_user = select(User).where(User.username == user.username)
        db_user = session.exec(find_user).first()

        if not db_user or not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({"sub": db_user.username})
        return Token(access_token=token, token_type="bearer")
    
@router.get("/me", response_model=UserRead, tags=["users"])
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/users/{user_id}", response_model=UserRead, tags=["users"])
def update_user(user_id: int, user: UserUpdate, session: Session = Depends(lambda: Session(engine))):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        db_user.adhar_no = user.adhar_no
        db_user.user_role = user.user_role
        
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user