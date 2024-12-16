from sqlalchemy.orm import Session
from app.models import LTEData
from app.schemas import LTEDataModel
from datetime import datetime

def convert_to_unix_timestamp(time_str: str) -> int:
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    return int(dt.timestamp())

def save_lte_data(db: Session, lte_data_list: list[LTEDataModel]):
    db_records = [
        LTEData(
            rsrpLte=lte_data.rsrpLte,
            rsrqLte=lte_data.rsrqLte,
            asuLevelLte=lte_data.asuLevelLte,
            levelLte=lte_data.levelLte,
            operatorLte=lte_data.operatorLte,
            mncLte=lte_data.mncLte,
            mccLte=lte_data.mccLte,
            time=convert_to_unix_timestamp(lte_data.time),
            latitude=lte_data.latitude,
            longitude=lte_data.longitude
        ) 
        for lte_data in lte_data_list
    ]

    db.add_all(db_records)
    db.commit()

    return db_records