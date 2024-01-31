import uvicorn
from fastapi import FastAPI, Request, Response, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from sqlalchemy import create_engine, exc
import os

load_dotenv()

DB_CONN = os.getenv('DB_CONN')

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    if request.method in ["POST", "PUT", "PATCH"]:
        content = await request.body()
        if content:
            return Response("Request body not allowed", status_code=400)
    response = await call_next(request)
    return response

print('============')
@app.get("/healthz")
def fetch_data() -> JSONResponse:
    try:
        print(f"{DB_CONN}") 
        engine = create_engine(DB_CONN) 
        engine.connect()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return JSONResponse(content={'status': 'ok'},headers={"Cache-Control": "no-cache"})


