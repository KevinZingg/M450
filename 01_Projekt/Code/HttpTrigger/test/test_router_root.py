from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    respsonse = client.get("/")
    assert respsonse.status_code == 200

def test_contact():
    respsonse = client.get("/contact")
    assert respsonse.status_code == 200


# Why dont work?
def test_url_haus():
    respsonse = client.get("/url_haus?domain=www.seyhanaluminyum.com")
    assert respsonse.status_code == 200

