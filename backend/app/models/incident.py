from sqlalchemy import Column, Integer, String
from app.services.db import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    component_id = Column(String)
    status = Column(String)
    severity = Column(String)

Base.metadata.create_all(bind=engine)
