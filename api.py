
import requests
 
URL = "https://api.frankfurter.app"
 
def get_exchange_rate(from_currency, to_currency):
    
    url = f"{URL}/latest"
    params = {
        "from": from_currency,
        "to": to_currency,
    }
 
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # raises an error if the request failed
    except requests.exceptions.RequestException as error:
        raise ValueError(f"Could not reach the currency API: {error}")
 
    data = response.json()
 
    rates = data.get("rates", {})
 
    if to_currency not in rates:
        raise ValueError(
            f"Could not find exchange rate for '{to_currency}'. "
            "Check that the currency code is correct (e.g. USD, EUR, GBP)."
        )
 
    return rates[to_currency]
 
 
def get_supported_currencies():
    
    url = f"{URL}/currencies"
 
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        raise ValueError(f"Could not reach the currency API: {error}")
 
    return response.json()