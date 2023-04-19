from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Bienvenido a UF-API"

