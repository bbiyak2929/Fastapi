from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
  name: str
  price : int
  
  
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str , q:str | None = None):
  item = Item(name="test_item", price=10)
  item_dict = item.model_dump()
  
  
  return templates.TemplateResponse(
    request=request,
    name="item.html",
    context={"id": id, "q_str" : q, "item" : item, "item_dict": item_dict}
    )