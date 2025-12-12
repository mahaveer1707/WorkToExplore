from app import create_app

def test_home_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/api/")
    assert response.status_code == 200

def test_valid_country_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/api/country/US")
    assert response.status_code == 200
