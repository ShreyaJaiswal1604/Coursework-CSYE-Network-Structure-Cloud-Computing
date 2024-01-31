from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from sqlalchemy import create_engine, exc
import os
import psycopg2
# from psycopg2 import OperationalError

# Loading environment variables from .env file
load_dotenv()


# Retrieving database connection string from environment variable
DB_CONN = os.getenv('DB_CONN')

#creating instance of FastAPI
app = FastAPI()

#Middleware function to check request body.
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):

    
    data = await request.body()
    if request.method in ["POST", "PUT", "PATCH","HEAD"]:
        if data or request.query_params:
            
            return Response("{}",status_code=400)
        else:
            return Response("{}",status_code=405)
    else:
        if data or request.query_params:
            return Response("{}",status_code=400)

    response = await call_next(request)
    return response


#Endpoint function to check request body.
@app.get("/healthz")
def fetch_data() -> JSONResponse:



    try:
        engine = create_engine(DB_CONN) 
        engine.connect()
        print(f"DB Connected Successfuly")
    except Exception as e:
        return Response("{}", status_code=503)
    #HTTPException(status_code=500, detail=str(e))
    
    return JSONResponse(content={},headers={"Cache-Control": "no-cache, no-store, must-revalidate"})




