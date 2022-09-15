from fastapi import APIRouter, Response
from src.config.bd import engine
from starlette.status import HTTP_404_NOT_FOUND
'''   utils   '''
from src.utils.selector import selector

from typing import List

data = APIRouter()

@data.get("/")
def get_hello():
    return {'hello':'world'}

@data.get("/api/{table}/")
def get_Analitica(table):
    with engine.connect() as con:
        data= selector(table)
        try:
            result= con.execute(data.select()).fetchall()
            return result
        except:
            return Response(status_code=HTTP_404_NOT_FOUND)

@data.get("/api/{table}/{id}")
def get_Analitica_id(table,id:str):
    with engine.connect() as con:
        data= selector(table) 
        try:
            result= con.execute(data.select().where(data.c.id==id)).first()
            return result
        except:
            return Response(status_code=HTTP_404_NOT_FOUND)
