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
  
 
@app.get("/item_gubun")
async def read_item_by_gubun(request: Request, gubun: str):
    item = Item(name="test_item_02", price=4.0)
    
    return templates.TemplateResponse(
        request=request, 
        name="item_gubun.html", 
        context={"gubun": gubun, "item": item}
    )

@app.get("/all_items", response_class=HTMLResponse)
async def read_all_items(request: Request):
    all_items = [Item(name="test_item_" +str(i), price=i) for i in range(5) ]
    print("all_items:", all_items)
    return templates.TemplateResponse(
        request=request, 
        name="item_all.html", 
        context={"all_items": all_items}
    )
    
@app.get("/read_safe", response_class=HTMLResponse)
async def read_safe(request: Request):
    html_str = '''
    <ul>
    <li>튼튼</li>
    <li>저렴</li>
    </ul>
    '''
    return templates.TemplateResponse(
        request=request, 
        name="read_safe.html", 
        context={"html_str": html_str}
    )