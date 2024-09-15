from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class item(BaseModel):
  name: str
  description: str | None = None
  age: int 
  tax: float | None = None
  


@app.post("/items")
async def create_item(item: item):
  return item


@app.post("items_tax/")
async def create_item_tax(item: item):
  item_dict = item.model_dump()
  #파이썬 딕셔너리
  
  if item.tax:
    age = item.age  + item.tax
    item_dict.update({age})
  return item_dict



class User(BaseModel):
  username: str
  full_nmae: str | None = None
  
  
@app.put("/items_mt/{item_id}")
async def update_item_mt(item_id: int, item: item, user : User):
  return 0
