from datetime import date
from unicodedata import name
from pydantic import BaseModel
from typing import Optional

class general_schema(BaseModel):
    id: Optional[str]
    '''FK'''
    id_area_analitica:int
    id_formato:int
    id_estado:int
    id_proveedor:int
    '''Data'''
    name: str
    lote:Optional[str]
    fecha_ingreso:Optional[str]
    fecha_vencimiento:Optional[str]
    cod_barra:Optional[str]
    cantidad:Optional[int]

class element_schema(BaseModel):
    id: Optional[str]
    name:str