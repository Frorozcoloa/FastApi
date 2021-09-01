from fastapi import APIRouter, HTTPException, exceptions
from config.db import conn
from models.index import vehiculos
from schemas.index import Vehiculo

VehiculoAPI = APIRouter()

@VehiculoAPI.get("/")
async def read_all_data():
    return conn.execute(vehiculos.select()).fetchall()

@VehiculoAPI.get("/{celda}")
async def read__data(celda:int):
    valor = conn.execute(vehiculos.select().where(vehiculos.c.celda == celda)).fetchall()
    if valor:
        return valor
    else:
        raise HTTPException(status_code=404, detail="item no encotrado")
        

@VehiculoAPI.post("/")
async def write_data(vehiculo:Vehiculo):
    try:
        conn.execute(vehiculos.insert().values(
            celda=vehiculo.celda,
            placa=vehiculo.placa,
        ))
        return conn.execute(vehiculos.select()).fetchall()
    except :
         raise HTTPException(status_code=404, detail="Celda ocupada")

@VehiculoAPI.put("/{celda}")
async def update_data(celda:int, vehiculo:Vehiculo):

        conn.execute(vehiculos.update().where(vehiculos.c.celda == celda).values(
            placa=vehiculo.placa,
        ))
        values = conn.execute(vehiculos.select().where(vehiculos.c.celda == celda)).fetchall()
        if values:
            return values
        else:
            raise HTTPException(status_code=404, detail="item no encotrado")


@VehiculoAPI.delete("/{celda}")
async def remove_vehiculo(celda:int):
    conn.execute(vehiculos.delete().where(vehiculos.c.celda==celda))
    return conn.execute(vehiculos.select()).fetchall()