from fastapi import WebSocket, WebSocketDisconnect, Depends
from pydantic import ValidationError
from app.schemas import LTEDataModel
from app.crud import save_lte_data
from app.database import get_db
from sqlalchemy.orm import Session
import logging
import os

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename="logs/server.log",
    filemode="a",
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    logging.info(f"Новое подключение: {websocket.client}")
    try:
        while True:
            data = await websocket.receive_text()
            logging.info(f"Получено сообщение: {data}")
            try:
                lte_data = LTEDataModel.parse_raw(data)
                save_lte_data(db, lte_data)
                await websocket.send_text("Данные успешно получены и сохранены на сервере.")
            except ValidationError as e:
                logging.error(f"Ошибка валидации: {e}")
                await websocket.send_text(f"Ошибка валидации: {e}")
    except WebSocketDisconnect:
        logging.info(f"Подключение закрыто: {websocket.client}")