from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_wrong_endpoint():
    response = client.get("/uf/")
    assert response.status_code == 404
    assert response.json() == {"detail":"Not Found"}

def test_last_ufs():
    response = client.get("/last_ufs")
    assert response.status_code == 200
    data = response.json()
    assert "2023-01-01" in data
    assert data["2023-01-01"] == "35.122,26"

def test_ufs_year():
    response = client.get("/ufs/2022")
    assert response.status_code == 200
    data = response.json()
    assert "2022-01-01" in data
    assert data["2022-01-01"] == "30.996,73"

def test_ufs_failed_year():
    response = client.get("/ufs/1800")
    assert response.status_code == 400
    assert response.json() == {"detail": "The year must be within the range of 2013 to current year"}

def test_uf_date():
    response = client.get("/uf/2023-04-01")
    assert response.status_code == 200
    assert response.json() == "35.574,33"

def test_uf_date_failed():
    response = client.get("/uf/2023-12-01")
    assert response.status_code == 404
    assert response.json() == {"detail": "There is no fomento unit for that date."}

def test_uf_date_wrong_year():
    response = client.get("/uf/2021-12-31")
    assert response.status_code == 400
    assert response.json() == {"detail": "The year date must be equal to current year"}

def test_invalid_env_uf_url(monkeypatch):
    monkeypatch.setenv("SII_UF_URL", "https://www.sii.cl/valores_y_fechas/uf/")
    response = client.get("/uf/2023-02-01")
    assert response.status_code == 500
    message = {
        "detail":
            "An error has occurred while trying to obtain the units of fomento. 404 Client Error: Not Found for url: https://www.sii.cl/valores_y_fechas/uf/"
    }
    assert response.json() == message
