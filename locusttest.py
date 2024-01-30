from locust import HttpUser, task, between


class QuickStart(HttpUser):
    wait_time = between(3,10)
    host = "http://localhost:8000"
    @task(1)
    def test_root(self):
        self.client.get("/")


    @task(5)
    def test_hello(self):
        self.client.get("/hallo")