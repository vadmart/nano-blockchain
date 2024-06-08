import unittest
from datetime import datetime, timedelta

import pytest

import main
from main import BlockInfo


class Block_HashTest(main.Block):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def hash(self):
        if self.nonce >= 1000:
            return "00000abcdefasfsdfsdaffaghijklmnop"
        return "abcdefasfsdfsdaffaghijklmnop"


class Block_HashTestFactory(main.BlockFactory):

    @staticmethod
    def generate_block(data: BlockInfo = None, timestamp: float = None, previous_hash: str = None):
        return Block_HashTest(data=data, timestamp=timestamp, previous_hash=previous_hash)


class TestBlock:
    # def test_block_without_data(self):
    #     block = main.Block()
    #     assert isinstance(block.timestamp, float)
    #     assert block.data is None
    #     assert isinstance(block.nonce, int)
    #     assert isinstance(block.previous_hash, str | None)

    def test_block_hash_is_correct(self):
        timestamp = datetime.now().timestamp()
        block1 = main.Block(timestamp=timestamp)
        block2 = main.Block(timestamp=timestamp)
        assert block1.hash == block2.hash
        block3 = main.Block(timestamp=timestamp + 100)
        assert block1.hash != block3.hash

    def test_proof_of_work_with_5_difficulty(self):
        block = Block_HashTest()
        with pytest.raises(ValueError):
            block.proof_of_work(1)
        block.proof_of_work()
        assert block.nonce == 1000
        assert block.hash[:5] == "00000"


class TestBlockFactory:
    def test_block_factory(self):
        block = main.BlockFactory.generate_block()
        assert isinstance(block, main.Block)


class TestBlockchain:
    block_factory = Block_HashTestFactory

    def test_blockchain_has_initial_block_with_none_previous_hash(self):
        blockchain = main.Blockchain(block_factory=self.block_factory)
        assert len(blockchain.chain) == 1
        assert blockchain.chain[0].previous_hash is None
        assert blockchain.chain[0].data is None

    def test_mine_block(self):
        blockchain = main.Blockchain(block_factory=self.block_factory)
        blockchain.mine_block()
        last_block = blockchain.chain[-1]
        previous_block = blockchain.chain[-2]
        assert last_block.previous_hash == previous_block.hash

    def test_mine_block_with_data(self):
        blockchain = main.Blockchain(block_factory=self.block_factory)
        block_data = BlockInfo(
            sender="Oleg",
            receiver="Matt",
            amount=500
        )
        blockchain.mine_block(data=block_data)
        assert blockchain.chain[-1].data == block_data


if __name__ == '__main__':
    unittest.main()
