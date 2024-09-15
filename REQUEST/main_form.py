from fastapi import FastAPI, Form 
from pydantic import BaseModel 
from typing import Annotated
app = FastAPI()


@app.post("/login")
async def login(username: str = Form(), 
                email: str = Form(),
                country : Annotated[str,Form()] = None):
  return {"username" : username,
          "email" : email,
          "country" : country}
  
  
