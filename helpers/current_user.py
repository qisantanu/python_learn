from fastapi.security import OAuth2PasswordBearer
from helpers.json_wt import decode_access_token
from jose import JWTError
from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from database.database import engine
from models.user_model import User

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_schema), session: Session = Depends(lambda: Session(engine))):
    with Session(engine) as session:
        try:
            payload = decode_access_token(token)
            username: str = payload.get("sub")

            if username is None:
                raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        
        # Fetch the user from the database
        user = session.exec(select(User).where(User.username == username)).first()
        if user is None or not user:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        
        return user