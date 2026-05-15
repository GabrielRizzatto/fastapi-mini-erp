from sqlalchemy.orm import Session
from models.user import User

def get_user_by_email(email: str, session: Session):
    return session.query(User).filter(User.email == email).first()

def save_user(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user