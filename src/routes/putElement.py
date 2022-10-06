from fastapi import APIRouter
from typing import List

from src.model.product import producto

'''  schemas  '''
from src.schemas.general_schema import element_schema, general_schema

'''  conexion BD   '''
from src.config.bd import engine

'''   utils   '''
from src.utils.selector import selector

putElement = APIRouter()

@putElement.put("/api/updateProduct/{area_id}",response_model=element_schema)
def update_Analitica(data_update:general_schema,id:str):
    with engine.connect() as con:
        con.execute(producto.update().values(name=data_update.name,
                                            lote=data_update.lote,
                                            fecha_ingreso=data_update.fecha_ingreso,
                                            fecha_vencimiento=data_update.fecha_vencimiento,
                                            cod_barra=data_update.cod_barra,
                                            cantidad=data_update.cantidad).where(producto.c.id==id))
        result= con.execute(producto.select().where(producto.c.id==id)).first()
        return result


@putElement.put("/api/update/{table}/{area_id}",response_model=element_schema)
def update_Analitica(table,data_update:element_schema,id:str):
    with engine.connect() as con:
        data=selector(table)
        con.execute(data.update().values(name=data_update.name).where(data.c.id==id))
        result= con.execute(data.select().where(data.c.id==id)).first()
        return result