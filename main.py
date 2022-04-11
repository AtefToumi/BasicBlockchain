import os

from fastapi import FastAPI
from fastapi.responses import FileResponse

path = "/home/atef/PycharmProjects/BasicBlockchain"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/blockchain/{block_name}")
async def show_block(block_name: str):
    file_path = os.path.join(path, block_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}
