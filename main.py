# Currency Converter

rates = {
    "USD": 1.00,
    "INR": 96.50,
    "EUR": 0.88,
    "GBP": 0.75
}

amount = float(input("Enter amount: "))
from_currency = input("From Currency (USD/INR/EUR/GBP): ").upper()
to_currency = input("To Currency (USD/INR/EUR/GBP): ").upper()

if from_currency in rates and to_currency in rates:
    # Convert to USD first
    usd = amount / rates[from_currency]

    # Convert USD to target currency
    converted = usd * rates[to_currency]

    print(f"\n{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Invalid currency code!")