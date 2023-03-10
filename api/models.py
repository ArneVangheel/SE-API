from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Codes(Base):
    __tablename__ = "codes"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    uses = Column(Integer, index=True)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
