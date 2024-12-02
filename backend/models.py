from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    google_id = Column(String, nullable=True)
    interest_tags = Column(ARRAY(String), default=[])
    
    liked_programs = relationship("ProgramLike", back_populates="user")

class Program(Base):
    __tablename__ = "programs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    platform = Column(String, nullable=False)  # online/F2F
    date_time = Column(DateTime(timezone=True), server_default=func.now())
    registration_method = Column(String)
    categories = Column(ARRAY(String))
    description = Column(String, nullable=True)
    
    likes = relationship("ProgramLike", back_populates="program")

class ProgramLike(Base):
    __tablename__ = "program_likes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    program_id = Column(Integer, ForeignKey('programs.id'))
    liked_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="liked_programs")
    program = relationship("Program", back_populates="likes")
