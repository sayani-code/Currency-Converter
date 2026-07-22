
rates = {
    "USD": 1.00,
    "INR": 96.50,
    "EUR": 0.88,
    "GBP": 0.75
}

def get_amount():
    amount = float(input("Enter amount: "))
    return amount


def get_currency(currency_ip):
    currency = input(currency_ip).upper()
    return currency


def convert_currency(amount, from_currency, to_currency):
    usd = amount / rates[from_currency]  #amount->USD
    converted = usd * rates[to_currency] #USD->to_currency
    return converted


def display_result(amount, from_currency, to_currency, converted):
    print(f"\n{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")


# Main Program
amount = get_amount()
from_currency = get_currency("From Currency (USD/INR/EUR/GBP): ")
to_currency = get_currency("To Currency (USD/INR/EUR/GBP): ")

if from_currency in rates and to_currency in rates:
    result = convert_currency(amount, from_currency, to_currency)
    display_result(amount, from_currency, to_currency, result)
else:
    print("Invalid currency code!")