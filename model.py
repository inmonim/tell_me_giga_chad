from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime, String

class Base(DeclarativeBase):
    pass

class Log(Base):
    
    __tablename__ = "gpt_log"
    
    log_id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String(255), nullable=False)
    answer = Column(String(1000))
    token = Column(Integer, nullable=False)