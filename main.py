import hashlib
from dataclasses import dataclass
from datetime import datetime
from typing import Type

from fastapi import FastAPI, Response


@dataclass
class BlockInfo:
    sender: str = ""
    receiver: str = ""
    amount: int = 0


class Block:
    def __init__(self, data: BlockInfo = None, timestamp: float = None, previous_hash: str = None):
        self.timestamp = timestamp or datetime.now().timestamp()
        self.data = data
        self.nonce = 0
        self.previous_hash = previous_hash

    @property
    def hash(self):
        hash_value = hashlib.sha256()
        hash_value.update(str(self.timestamp).encode())
        hash_value.update(str(self.data).encode())
        hash_value.update(str(self.nonce).encode())
        hash_value.update(str(self.previous_hash).encode())
        return hash_value.hexdigest()

    def proof_of_work(self, difficulty=5):
        if difficulty < 2:
            raise ValueError("'difficulty' cannot be less than 2")
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1


class BlockFactory:
    @staticmethod
    def generate_block(data: BlockInfo = None, timestamp: float = None, previous_hash: str = None):
        return Block(data=data, timestamp=timestamp, previous_hash=previous_hash)


class Blockchain:
    def __init__(self, block_factory: Type[BlockFactory]):
        self.__chain: list[Block] = []
        self.block_factory = block_factory
        self.mine_block()

    def mine_block(self, data: BlockInfo = None, timestamp: float = None):
        last_block_hash = self.__chain[-1].hash if len(self.__chain) > 0 else None
        block = self.block_factory.generate_block(data=data, timestamp=timestamp, previous_hash=last_block_hash)
        block.proof_of_work()
        self.__chain.append(block)

    @property
    def chain(self) -> list[Block]:
        return self.__chain.copy()


blockchain = Blockchain(BlockFactory)
app = FastAPI()


@app.get("/blockchain")
def get_blockchain():
    return {"blockchain": blockchain.chain, "length": len(blockchain.chain)}


@app.get("/blockchain/mine")
def mine_block():
    blockchain.mine_block()
    return Response(status_code=204)


@app.get("/blockchain/block/{item_id}")
def get_blockchain_block(item_id: int, response: Response):
    try:
        return {"block": blockchain.chain[item_id - 1]}
    except IndexError:
        response.status_code = 404
        return {"error": "Item was not found"}


@app.post("/blockchain/make-transaction")
def make_transaction(data: BlockInfo, response: Response):
    blockchain.mine_block(data=data)
    response.status_code = 201
    return data
