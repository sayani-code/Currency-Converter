from converter import convert
from utils import is_valid_amount, is_valid_currency_name, format_result
 
 
def get_amount_from_user():
    while True:
        text = input("Enter the amount to convert: ").strip()
        if is_valid_amount(text):
            return float(text)
        print("That is not valid amount.Try again!\n")
 
 
def get_currency_from_user(prompt):
    while True:
        currency_name = input(prompt).strip().upper()
        if is_valid_currency_name(currency_name):
            return currency_name
        print("Please enter a valid 3-letter currency code,(USD / EUR / GBP / JPY /INR).\n")
 
 
def run():
    print("-" * 10," Currency Converter ","-" * 10)
    print("Tip: Use 3-letter codes like .\n")
 
    amount = get_amount_from_user()
    from_currency = get_currency_from_user("Convert FROM which currency?(USD / EUR / GBP / JPY /INR)\n")
    to_currency = get_currency_from_user("Convert TO which currency?(USD / EUR / GBP / JPY /INR)\n")
 
    print("\nFetching the latest exchange rate...\n")
 
    try:
        converted_amount, rate = convert(amount, from_currency, to_currency)
    except ValueError as error:
        print(f"Error: {error}")
        return
 
    print(format_result(amount, from_currency, converted_amount, to_currency, rate))
 
 
if __name__ == "__main__":
    run()