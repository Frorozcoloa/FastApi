from fastapi import FastAPI
from routes.index import VehiculoAPI, facturaApi
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(VehiculoAPI)
app.include_router(facturaApi)

origins  = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

