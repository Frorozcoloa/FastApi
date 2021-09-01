from fastapi import FastAPI
from routes.index import VehiculoAPI

app = FastAPI()
app.include_router(VehiculoAPI)