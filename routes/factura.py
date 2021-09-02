from fastapi import APIRouter, HTTPException, exceptions
from sqlalchemy.sql.expression import text
from config.db import conn
from models.index import vehiculos
from sqlalchemy import text
from datetime import datetime


facturaApi = APIRouter()

@facturaApi.post('/{celda}')
async def create_facture(celda:int):
    fecha = conn.execute(vehiculos.select().where(vehiculos.c.celda ==celda)).first()[2]
    tiempo = datetime.now() - fecha 
    precio = tiempo.total_seconds()*100/60
    print(round(precio))