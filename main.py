# FastAPI tutorial
# https://coffeebytes.dev/python-fastapi-el-mejor-framework-de-python/

# Fetch SQLite DB with FastAPI:
# https://stackoverflow.com/questions/65270624/how-to-connect-to-a-sqlite3-db-file-and-fetch-contents-in-fastapi


from fastapi import FastAPI
from typing import Optional

app = FastAPI()

items = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup_event():
    items[1] = {"name": "Foo Fighters"}
    items[2] = {"name": "High Voltage"}
    items[3] = {"name": "Serious Business"}
    items[4] = {"name": "Say Hello"}


@app.get("/items")
async def get_items():
    return items


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items[item_id]