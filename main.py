from fastapi import FastAPI


#from src.routes.getProduct import product
from src.routes.getElement import data
from src.routes.postElement import insert
from src.routes.deleteElement import delElement
from src.routes.putElement import putElement


app = FastAPI(title='Api Inventario')

app.include_router(data)
app.include_router(insert)
app.include_router(putElement)
app.include_router(delElement)