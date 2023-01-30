from typing import Optional
from config import CONFIG

from utils import open_markdown, open_page, open_template, error_404

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import Config, Server

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/markdowns", StaticFiles(directory="markdowns"), name="markdowns")

@app.get("/")
async def root():
    return await open_template("index.html")

@app.get("/include-page/{filename}")
async def templates(filename: Optional[str]=None):
    return await open_page(filename)

@app.exception_handler(404)
async def not_found(requests, exc):
    return await error_404()

def run():
    config = Config(app, host=CONFIG.host, port=CONFIG.port)
    server = Server(config=config)
    server.run()

if __name__ == "__main__":
    run()
