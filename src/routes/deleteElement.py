from fastapi import APIRouter, Response
from starlette.status import  HTTP_204_NO_CONTENT
from typing import List

from src.model.product import producto

'''  schemas  '''
from src.schemas.general_schema import element_schema, general_schema

'''  conexion BD   '''
from src.config.bd import engine

'''   utils   '''
from src.utils.selector import selector

delElement = APIRouter()


@delElement.delete("/api/deleteProduct/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_Analitica(id: str):
    with engine.connect() as con:
        con.execute(producto.delete().where(producto.c.id==id))
        return Response(status_code=HTTP_204_NO_CONTENT)

@delElement.delete("/api/deleteDefinition/{table}/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_Analitica(table,id: str):
    with engine.connect() as con:
        data= selector(table)
        con.execute(data.delete().where(producto.c.id==id))
        return Response(status_code=HTTP_204_NO_CONTENT)
