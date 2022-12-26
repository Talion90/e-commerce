import uvicorn
from fastapi import FastAPI

from config import AppCfg
from routers import goods


app = FastAPI(title="E-Commerce")

app.include_router(goods.router)


@app.get('/')
async def index():
    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run(app, host=AppCfg.host, port=AppCfg.port, reload=True)
