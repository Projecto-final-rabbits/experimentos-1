from fastapi import FastAPI
from bodega.service.bodega_service import bodega_router
from ventas.service.ventas_service import ventas_router
from compras.service.compras_service import compras_router

app = FastAPI()

app.include_router(bodega_router, prefix="/bodega", tags=["Bodega"])
app.include_router(ventas_router, prefix="/ventas", tags=["Ventas"])
app.include_router(compras_router, prefix="/compras", tags=["Compras"])

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI Monorepo!"}