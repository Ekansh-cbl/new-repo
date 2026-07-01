from fastapi.testclient import TestClient

from app.core import create_app


client = TestClient(create_app())


def test_dashboard_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "DualCam Ops" in response.text
    assert "Live Monitoring Dashboard" in response.text


def test_register_page_loads_and_posts():
    response = client.get("/register")
    assert response.status_code == 200
    assert "Capture Progress" in response.text

    shot = client.post("/capture", follow_redirects=True)
    assert shot.status_code == 200
    assert "Capture session started" in shot.text

    posted = client.post(
        "/register",
        data={"full_name": "Test User", "notes": "Blue jacket", "camera": "Inbuilt Camera"},
    )
    assert posted.status_code == 200
    assert "Saved Test User" in posted.text


def test_people_and_training_pages_load():
    people = client.get("/people")
    training = client.get("/training")
    assert people.status_code == 200
    assert training.status_code == 200
    assert "Anonymous IDs" in people.text
    assert "Model control center" in training.text


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
