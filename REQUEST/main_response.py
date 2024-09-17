from fastapi import FastAPI, Request, status, Form
from fastapi.responses import (
  JSONResponse,
  HTMLResponse,
  RedirectResponse
)
from pydantic import BaseModel
app = FastAPI()

@app.get("/resp_json/{item_id}", response_class=JSONResponse)
async def response_json(item_id: int , q: str | None = None):
  return JSONResponse(content={"message" : "hi",
                               "item_id" : item_id})
  
  
@app.get("/resp_html/{item_id}", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def response_html(item_id: int , item_name: str | None = None):
  html_str = "html"
  return HTMLResponse(html_str)


@app.post("/create_redirect")
async def create_item(item_id:int = Form(), item_name : str = Form()):
  print(f"item_id: {item_id} item name : {item_name}")
  
  return RedirectResponse(url=f"resp_html/{item_id}?item_name = {item_name}")

class Item(BaseModel):
  name: str
  description: str
  price: float
  tax: float | None = None

class ItemResp(BaseModel):
  name: str
  description: str
  price_with_tax: float
  
  
@app.post("/create_item", response_model=ItemResp)
async def create_item_model(item: Item):
  if item.tax:
    price_with_tax = item.price + item.tax
    
  else:
    price_with_tax = item.price
    
  
  item_resp = ItemResp(name = item.name,
           description=item.description,
           price_with_tax=price_with_tax)
  
  
  return item_resp