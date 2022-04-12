import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from block import Block
from user import User
from verify_block import verify_block

path = "/home/atef/PycharmProjects/BasicBlockchain"

app = FastAPI()


class BlockRequest(BaseModel):
    last_block: str
    new_block: str
    transaction: str
    id: str
    passphrase: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/blockchain/{block_name}")
async def show_block(block_name: str):
    file_path = os.path.join(path, block_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}


@app.get("/blockchain/verify/{block_name}")
async def verify_block_file(block_name: str):
    file_path = os.path.join(path, block_name)
    if os.path.exists(file_path):
        return verify_block(block_name)


@app.post("/blockchain/add_block")
async def create_block(block: BlockRequest):
    new_block = Block(block.last_block, block.new_block, block.transaction)
    return new_block.add_block(User(block.id, block.passphrase))
