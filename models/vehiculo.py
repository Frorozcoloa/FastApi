from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

vehiculos = Table('vehiculos', meta,
                 Column('celda', Integer, primary_key=True),
                 Column('placa', String(255)),
                 Column('fecha', DateTime),
                 )