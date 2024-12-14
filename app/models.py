from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class LTEData(Base):
    __tablename__ = "lte_data"

    id = Column(Integer, primary_key=True, index=True)
    rsrpLte = Column(Integer, nullable=False)
    rsrqLte = Column(Integer, nullable=False)
    asuLevelLte = Column(Integer, nullable=False)
    levelLte = Column(Integer, nullable=False)
    operatorLte = Column(String, nullable=True)
    mncLte = Column(String, nullable=True)
    mccLte = Column(String, nullable=True)
    time = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)