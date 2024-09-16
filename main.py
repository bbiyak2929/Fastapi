from fastapi import FastAPI


app = FastAPI(
  title="FastAPI 인강 실습용 레포지토리 야삐"
)


@app.get("/")
async def root():
  return {"message" : "yabbi"}

