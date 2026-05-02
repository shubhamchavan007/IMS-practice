from sqlalchemy import Column, Integer, String, DateTime, Text
from app.services.db import engine
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    component_id = Column(String)
    status = Column(String)
    severity = Column(String)
    
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)

    rca = Column(Text, nullable=True)
    mttr = Column(Integer, nullable=True)  # store in seconds
Base.metadata.create_all(bind=engine)
