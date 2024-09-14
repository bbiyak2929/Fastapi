from fastapi import FastAPI
from enum import Enum

app = FastAPI()



@app.get('/item/{item_id}')

async def read_item(item_id: int):
  return {"item_id": item_id}

class ItemType(str, Enum):
  small = "small"
  medium = "medium"
  large = "large"
  

@app.get("/items/type/{item_type}")
async def get_item_type(item_type: ItemType):
  return {"message": f"item type is {item_type}"}