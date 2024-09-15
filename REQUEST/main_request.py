from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/items")
async def read_item(request: Request):
  cl = request.client.host
  header = request.headers
  qp = request.query_params
  url = request.url
  pp = request.path_params
  http = request.method
  
  
