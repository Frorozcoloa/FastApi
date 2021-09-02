from fastapi import APIRouter, HTTPException, exceptions
from sqlalchemy.sql.expression import text
from config.db import conn
from models.index import vehiculos
from sqlalchemy import text
from datetime import datetime

from Factura.index import create_pdf


facturaApi = APIRouter()

@facturaApi.post('/precio/{celda}')
async def create_facture(celda:int):
    hoy = datetime.now()
    values = conn.execute(vehiculos.select().where(vehiculos.c.celda ==celda)).fetchall()
    tiempo = hoy - values[0][2] 
    precio = tiempo.total_seconds()*100/60
    datos = {'placa':values[0][1], 'fecha_in':values[0][2], 'fecha_out': hoy, 'total': precio, 'celda':values[0][0] }
    create_pdf(datos)

@facturaApi.get('/precio/{celda}')
async def get_precio(celda:int):
    hoy = datetime.now()
    values = conn.execute(vehiculos.select().where(vehiculos.c.celda ==celda)).fetchall()
    tiempo = hoy - values[0][2] 
    precio = tiempo.total_seconds()*100/60
    return {'Total': precio}

    
    
    