import logging
from datetime import datetime, timedelta

from fastapi.testclient import TestClient

import main

client = TestClient(main.app)
logger = logging.getLogger(__name__)


def test_create_block_with_difficulty_5_is_less_than_1_minute():
    for _ in range(100):
        start_time = datetime.now()
        client.post("/blockchain/mine?difficulty=5")
        assert datetime.now() - start_time < timedelta(minutes=1)
