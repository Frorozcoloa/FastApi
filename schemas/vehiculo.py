from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Vehiculo(BaseModel):
    id: Optional[int]
    placa:str
    fecha:datetime = datetime.now()
    celda:int 
