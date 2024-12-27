from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL - yahan apni database ka URL daalna hai
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Engine - Jo SQLAlchemy ko bataega ki kis database se connect karna hai
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal - Jo session banaega, jisse hum query run karenge
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base - Jo models se inherit hoga
Base = declarative_base()
