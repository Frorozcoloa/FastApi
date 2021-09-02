from fastapi import APIRouter, HTTPException, exceptions
from sqlalchemy.sql.expression import text
from config.db import conn
from models.index import vehiculos
from sqlalchemy import text
from datetime import datetime

from Factura.index import create_pdf


facturaApi = APIRouter()

@facturaApi.get('/precio/{celda}')
async def get_precio(celda:int):
    hoy = datetime.now()
    values = conn.execute(vehiculos.select().where(vehiculos.c.celda ==celda)).fetchall()
    tiempo = hoy - values[0][2] 
    precio = round(tiempo.total_seconds()*100/60,2)
    print(values[0][2])
    return {'celda':values[0][0], 'placa': values[0][1], 'fecha_in':values[0][2], 'fecha_out':hoy, 'total': precio }
    
    
    