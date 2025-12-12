from .data import COUNTRIES

class CountryService:

    @staticmethod
    def get_country_details(code: str):
        code = code.upper()
        if code in COUNTRIES:
            return COUNTRIES[code]
        return None
