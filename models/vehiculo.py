from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

vehiculos = Table('vehiculo', meta,
                 Column('id', Integer, primary_key=True),
                 Column('placa', String(255)),
                 Column('fecha', DateTime),
                 Column('celda', Integer)
                 )