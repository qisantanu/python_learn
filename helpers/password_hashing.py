from passlib.hash import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.using(rounds=12).hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.verify(password, hashed_password)