from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/address")
async def read_address(request: Request):
    return templates.TemplateResponse("address.html", {"request": request})


@app.get("/items")
async def read_items(request: Request):
    return templates.TemplateResponse("items.html", {"request": request})


@app.get("/buy-online")
async def read_buy_online(request: Request):
    return templates.TemplateResponse("buy_online.html", {"request": request})


@app.get("/how-to-use")
async def read_how_to_use(request: Request):
    return templates.TemplateResponse("how_to_use.html", {"request": request})


@app.get("/where-use")
async def read_where_use(request: Request):
    return templates.TemplateResponse("where_use.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

