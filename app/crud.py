from sqlalchemy.orm import Session
from .models import Item

def get_items(db: Session):
    return db.query(Item).all()

def create_item(db: Session, name: str, description: str):
    db_item = Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
