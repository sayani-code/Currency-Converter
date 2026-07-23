def is_valid_amount(text):
    #Check whether the ammount valid or not
    try:
        value = float(text)
        return value > 0
    except ValueError:
        return False
 
 
def is_valid_currency_name(currency_name):
    
    return isinstance(currency_name, str) and len(currency_name) == 3 and currency_name.isalpha()
 
 
def format_result(amount, from_currency, converted_amount, to_currency, rate):
    
    return (
        f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}\n"
        f"(1 {from_currency} = {rate:.4f} {to_currency})"
    )