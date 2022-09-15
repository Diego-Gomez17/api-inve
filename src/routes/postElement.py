from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from typing import List

from src.model.product import producto

'''  schemas  '''
from src.schemas.general_schema import element_schema, general_schema

'''  conexion BD   '''
from src.config.bd import engine

'''   utils   '''
from src.utils.selector import selector



insert = APIRouter()

@insert.post("/api/insertProduct/", status_code=HTTP_201_CREATED)
def create_Analitica(data_aA:general_schema):
    with engine.connect() as con:
        new_product= data_aA.dict()
        try:
            con.execute(producto.insert().values(new_product))
            return Response(status_code=HTTP_201_CREATED)
        except:
            print("los datos entregados no corresponden a los campos!!")
            return Response(status_code=HTTP_400_BAD_REQUEST)


@insert.post("/api/insertDefinition/{table}/", status_code=HTTP_201_CREATED)
def create_Analitica(table,data_aB:element_schema):
    with engine.connect() as con:
        data= selector(table) 
        new_element= data_aB.dict()
        try:
            con.execute(data.insert().values(new_element))
            return Response(status_code=HTTP_201_CREATED)
        except:
            print("los datos entregados no corresponden a los campos!!")
            return Response(status_code=HTTP_400_BAD_REQUEST)