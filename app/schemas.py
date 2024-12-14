from pydantic import BaseModel, Field
from typing import List

class LTEDataModel(BaseModel):
    rsrpLte: int = Field(..., description="RSRP LTE")
    rsrqLte: int = Field(..., description="RSRQ LTE")
    asuLevelLte: int = Field(..., description="ASU Level LTE")
    levelLte: int = Field(..., description="Уровень сигнала LTE")
    operatorLte: str = Field(None, description="Оператор LTE")
    mncLte: str = Field(None, description="MNC LTE")
    mccLte: str = Field(None, description="MCC LTE")
    time: str = Field(..., description="Дата и время")
    latitude: float = Field(..., description="Широта")
    longitude: float = Field(..., description="Долгота")

class LTEDataList(BaseModel):
    jsonLteCellInfo: List[LTEDataModel]