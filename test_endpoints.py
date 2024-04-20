from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_get_blockchain():
    response = client.get('/blockchain')
    assert response.status_code == 200
    data = response.json()
    assert data.get("blockchain") is not None
    assert data.get("length") is not None
    assert data["length"] == 1


def test_blockchain_mine():
    response = client.get('/blockchain/mine')
    assert response.status_code == 204
    assert len(main.blockchain.chain) == 2


def test_blockchain_block():
    response = client.get('/blockchain/block/1')
    assert response.status_code == 200
    assert response.json().get("")
    response = client.get('/blockchain/block/98754654')
    assert response.status_code == 404
    assert response.json().get("error") is not None


def test_making_transaction_with_valid_data():
    data = {
        "sender": "Petia",
        "receiver": "Oleg",
        "amount": "500"
    }
    response = client.post('/blockchain/make-transaction', json=data)
    assert response.status_code == 201
    assert len(main.blockchain.chain) == 2
