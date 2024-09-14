from fastapi import FastAPI
from typing import Optional

app = FastAPI()


fake_item_db = [{"item_name": "Foo"}, {"item_name": "bar"}, {"item_name": "yabbi"}]

@app.get("/item/")

async def read_item(skip: int = 0, limit: int = 10):
  return fake_item_db[skip: skip + limit] 

@app.get("/items_nd/")
async def read_item_nd(skip: int , limit: int):
    return fake_item_db[skip: skip + limit] 
