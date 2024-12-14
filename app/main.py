from fastapi import FastAPI, Request, Depends, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database import Base, engine, get_db
from app.models import LTEData
from app.websocket import websocket_endpoint

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket, db = Depends(get_db)):
    await websocket_endpoint(websocket, db)