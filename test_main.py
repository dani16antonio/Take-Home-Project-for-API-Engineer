from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_get_meal():
    response = client.get('/menu/2022-5-10/carne')  #TODO: retest when remote databa is available
    assert response.status_code == 200

def test_meal_not_found():
    response = client.get('/menu/2022-5-10/carnes')  #TODO: retest when remote databa is available
    assert response.status_code == 404