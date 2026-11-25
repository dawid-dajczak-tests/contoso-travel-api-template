"""Testy dla Contoso Travel API."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_countries_zwraca_liste():
    """Lista krajów zawiera Hiszpanię."""
    response = client.get("/countries")
    assert response.status_code == 200
    assert "Spain" in response.json()


def test_cities_dla_hiszpanii():
    """Hiszpania ma w danych Sewillę."""
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    assert "Seville" in response.json()
