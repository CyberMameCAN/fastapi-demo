import pathlib
from fastapi import FastAPI
from pathlib import Path
from .calculator import enshuritsu

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/enshuritsu/montecalro/{calc_count}")
def read_montecalro(calc_count: int = 100):
    mypi = enshuritsu.montecarlo_method(calc_count)
    return {"PI=": mypi, "count": calc_count}

@app.get("/enshuritsu/gregory_prog/{calc_end}")
def read_gregory(calc_end: int = 1000):
    mypi = enshuritsu.gregory_progression(calc_end)
    return {"PI=": mypi, "count": calc_end}
