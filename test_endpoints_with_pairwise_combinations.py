from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_make_transaction_with_latin_sender_cyrillic_receiver_450_25_amount_and_3_difficulty():
    data = {
        "sender": "Michael",
        "receiver": "Іван",
        "amount": 450.25
    }
    difficulty = 3
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_latin_sender_latin_receiver_99999999999999999999999999999999999_amount_and_4_difficulty():
    data = {
        "sender": "Michael",
        "receiver": "Avriel",
        "amount": 99999999999999999999999999999999999
    }
    difficulty = 4
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_latin_sender_cyrillic_receiver_500_amount_and_5_difficulty():
    data = {
        "sender": "Michael",
        "receiver": "Іван",
        "amount": 500
    }
    difficulty = 5
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_cyrillic_sender_cyrillic_receiver_99999999999999999999999999999999999_amount_and_5_difficulty():
    data = {
        "sender": "Петр",
        "receiver": "Іван",
        "amount": 99999999999999999999999999999999999
    }
    difficulty = 5
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_cyrillic_sender_latin_receiver_500_amount_and_2_difficulty():
    data = {
        "sender": "Петр",
        "receiver": "Avriel",
        "amount": 500
    }
    difficulty = 2
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_cyrillic_sender_cyrillic_receiver_500_amount_and_3_difficulty():
    data = {
        "sender": "Петр",
        "receiver": "Іван",
        "amount": 500
    }
    difficulty = 3
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_cyrillic_sender_latin_receiver_450_25_amount_and_4_difficulty():
    data = {
        "sender": "Петр",
        "receiver": "Avriel",
        "amount": 450.25
    }
    difficulty = 4
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_cyrillic_sender_cyrillic_receiver_450_25_amount_and_5_difficulty():
    data = {
        "sender": "Петр",
        "receiver": "Іван",
        "amount": 450.25
    }
    difficulty = 5
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_cyrillic_sender_latin_receiver_99999999999999999999999999999999999_amount_and_2_difficulty():
    data = {
        "sender": "Петр",
        "receiver": "Avriel",
        "amount": 99999999999999999999999999999999999
    }
    difficulty = 2
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_latin_sender_latin_receiver_99999999999999999999999999999999999_amount_and_3_difficulty():
    data = {
        "sender": "Michael",
        "receiver": "Avriel",
        "amount": 99999999999999999999999999999999999
    }
    difficulty = 3
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]


def test_make_transaction_with_latin_sender_latin_receiver_500_amount_and_4_difficulty():
    data = {
        "sender": "Michael",
        "receiver": "Avriel",
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


def test_make_transaction_with_latin_sender_latin_receiver_450_25_amount_and_2_difficulty():
    data = {
        "sender": "Michael",
        "receiver": "Avriel",
        "amount": 450.25
    }
    difficulty = 2
    response = client.post(f'/blockchain/make-transaction?difficulty={difficulty}', json=data)
    assert response.status_code == 201
    response = client.get('/blockchain')
    last_block = response.json().get("blockchain")[-1]["data"]
    assert last_block["sender"] == data["sender"]
    assert last_block["receiver"] == data["receiver"]
    assert last_block["amount"] == data["amount"]