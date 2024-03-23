import unittest, main
from unittest.mock import patch
from datetime import datetime

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
    def generate_block(data: BlockInfo=None, timestamp: float = None, previous_hash: str = None):
        return Block_HashTest(data=data, timestamp=timestamp, previous_hash=previous_hash)

class TestBlock(unittest.TestCase):
    def test_block_without_data(self):
        block = main.Block()
        self.assertTrue(isinstance(block.timestamp, float))
        self.assertIsNone(block.data)
        self.assertTrue(isinstance(block.nonce, int))
        self.assertTrue(isinstance(block.previous_hash, str | None))

    def test_block_hash(self):
        timestamp = datetime.now().timestamp()
        block1 = main.Block(timestamp=timestamp)
        self.assertTrue(isinstance(block1.hash, str))
        self.assertTrue(len(block1.hash) == 64)
        block2 = main.Block(timestamp=timestamp)
        self.assertTrue(block1.hash == block2.hash)
        block3 = main.Block()
        self.assertFalse(block1.hash == block3.hash)

    def test_proof_of_work(self):
        block = Block_HashTest()
        self.assertRaises(ValueError, block.proof_of_work, 1)
        block.proof_of_work()
        self.assertTrue(block.nonce == 1000)
        self.assertTrue(block.hash[:5] == "00000")

class TestBlockFactory(unittest.TestCase):
    def test_block_factory(self):
        block = main.BlockFactory.generate_block()
        self.assertIsInstance(block, main.Block)

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.block_factory = Block_HashTestFactory

    def test_blockchain_has_initial_block(self):
        blockchain = main.Blockchain(block_factory=self.block_factory)
        self.assertEqual(1, len(blockchain.chain))

    def test_mine_block(self):
        blockchain = main.Blockchain(block_factory=self.block_factory)
        blockchain.mine_block()
        last_block = blockchain.chain[-1]
        previous_block = blockchain.chain[-2]
        self.assertTrue(last_block.previous_hash == previous_block.hash)


if __name__ == '__main__':
    unittest.main()
