from sqlalchemy.orm import Session
from app.models import LTEData
from app.schemas import LTEDataModel

def save_lte_data(db: Session, lte_data: LTEDataModel):
    db_data = LTEData(
        rsrpLte = lte_data.rsrpLte,
        rsrqLte = lte_data.rsrqLte,
        asuLevelLte = lte_data.asuLevelLte,
        levelLte = lte_data.levelLte,
        operatorLte = lte_data.operatorLte,
        mncLte = lte_data.mncLte,
        mccLte = lte_data.mccLte,
        time = lte_data.time,
        latitude = lte_data.latitude,
        longitude = lte_data.longitude
    )

    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    return db_data