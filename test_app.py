from app import app

def test_get_weather():
    client = app.test_client()
    response = client.get('/weather/London')
    assert response.status_code == 200
    assert b"London" in response.data

def test_add_favorite():
    client = app.test_client()
    response = client.post('/favorites', json={"city": "Paris"})
    assert response.status_code == 200
    assert b"Paris" in response.data

