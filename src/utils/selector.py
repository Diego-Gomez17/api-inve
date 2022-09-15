from src.model.areaAnalitica import  area_analitica
from src.model.estado import  estado
from src.model.formato import  formato
from src.model.proveedor import  proveedor
from src.model.product import  producto


def selector(table):
    if table==str(estado):
        return estado
    if table==str(area_analitica):
        return area_analitica
    if table==str(formato):
        return formato
    if table==str(proveedor):
        return proveedor
    if table==str(producto):
        return producto