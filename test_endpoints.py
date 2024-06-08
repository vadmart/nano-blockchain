from datetime import datetime

from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_get_blockchain():
    response = client.get('/blockchain')
    assert response.status_code == 200
    data = response.json()
    assert data.get("blockchain") is not None
    blockchain = data["blockchain"]
    assert isinstance(blockchain, list)
    chain = blockchain[0]
    assert isinstance(chain, dict)
    assert "timestamp" in chain
    assert "nonce" in chain
    assert "data" in chain
    assert "previous_hash" in chain
    assert data.get("length") is not None
    assert data["length"] == 1


def test_blockchain_mine():
    response = client.post('/blockchain/mine')
    assert response.status_code == 204
    assert len(main.blockchain.chain) == 2


def test_blockchain_mine_with_valid_difficulty():
    response = client.post('/blockchain/mine')
    assert response.status_code == 204
    response = client.post('/blockchain/mine?difficulty=4')
    assert response.status_code == 204


def test_blockchain_mine_with_difficulty_with_incorrect_type():
    response = client.post('/blockchain/mine?difficulty=herewego')
    assert response.status_code == 422
    response = client.post('/blockchain/mine?difficulty=3.5')
    assert response.status_code == 422


def test_blockchain_mine_with_difficulty_less_than_2():
    response = client.post('/blockchain/mine?difficulty=-3')
    assert response.status_code == 400
    error_detail = response.json()["detail"]
    assert error_detail == "Difficulty cannot be less than 2"


def test_blockchain_block():
    response = client.get('/blockchain/block/1')
    assert response.status_code == 200
    response = client.get('/blockchain/block/98754654')
    assert response.status_code == 404
    assert response.json().get("error") is not None


def test_making_transaction_with_valid_data():
    data = {
        "sender": "Petia",
        "receiver": "Oleg",
        "amount": 500
    }
    response = client.post('/blockchain/make-transaction', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_making_transaction_with_amount_with_incorrect_type():
    data = {
        "sender": "Petr",
        "receiver": "Oleg",
        "amount": "asdsad"
    }
    response = client.post('/blockchain/make-transaction', json=data)
    assert response.status_code == 422


def test_making_transaction_with_negative_amount():
    data = {
        "sender": "Petr",
        "receiver": "Oleg",
        "amount": -500
    }
    response = client.post('/blockchain/make-transaction', json=data)
    assert response.status_code == 400
    error_detail = response.json()["detail"]
    assert error_detail == "Amount cannot be less than or equal to 0"


def test_making_transaction_with_valid_data_and_4_difficulty():
    data = {
        "sender": "Petia",
        "receiver": "Oleg",
        "amount": 500
    }
    difficulty = 4
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_making_transaction_with_difficulty_less_than_2_and_invalid_amount():
    data = {
        "sender": "Petr",
        "receiver": "Oleg",
        "amount": -500
    }
    difficulty = 1
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert isinstance(detail, list)


def test_making_transaction_with_invalid_sender_and_receiver_values():
    data = {
        "sender": 14,
        "receiver": 123,
        "amount": 500
    }
    response = client.post('/blockchain/make-transaction', json=data)
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert isinstance(detail, list)
