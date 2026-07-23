from api import get_exchange_rate
 
 
def convert(amount, from_currency, to_currency):
    
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
 
    # No need to call the API if converting a currency to itself.
    if from_currency == to_currency:
        return amount, 1.0
 
    rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * rate
 
    return converted_amount, rate