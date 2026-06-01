from fastapi import FastAPI
from controller.entradas_controller import router as comprar_router


app = FastAPI()

app.include_router(comprar_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.start.main:app", reload=True)