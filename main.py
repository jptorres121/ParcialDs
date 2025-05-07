from fastapi import FastAPI

import usuarios
from database import crear_tablas
from usuarios import crear_usuario

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


crear_tablas()

app.include_router(usuarios.router)
