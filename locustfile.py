from locust import HttpUser, task


class RequestsUser(HttpUser):
    host = "http://127.0.0.1:8000"

    @task(1)
    def test_creating_block_with_difficulty_5_request(self):
        self.client.post("/blockchain/mine?difficulty=5")

    @task(1)
    def test_creating_a_transaction_with_difficulty_5_request(self):
        data = {
            "sender": "Peter",
            "receiver": "John",
            "amount": 500
        }
        self.client.post("/blockchain/make-transaction?difficulty=5", json=data)
