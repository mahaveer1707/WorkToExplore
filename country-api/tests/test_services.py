from app.service import CountryService

def test_valid_country():
    data = CountryService.get_country_details("IN")
    assert data["capital"] == "New Delhi"

def test_invalid_country():
    data = CountryService.get_country_details("XX")
    assert data is None
