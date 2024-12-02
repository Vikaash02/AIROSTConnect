from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/recommendation_db')

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, 
    poolclass=NullPool,  # Disable connection pooling
    pool_pre_ping=True
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Base class for declarative models
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
