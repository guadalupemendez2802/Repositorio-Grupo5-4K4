from fastapi import FastAPI
from controller.entradas_controller import router as comprar_router
from controller.compras_controller import router_compras


app = FastAPI()

app.include_router(comprar_router)
app.include_router(router_compras)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.start.main:app", reload=True)