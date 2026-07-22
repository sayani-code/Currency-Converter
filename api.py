import requests

url = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url)
data = response.json()

print("USD to INR =", data["rates"]["INR"])
print("USD to EUR =", data["rates"]["EUR"])
print("USD to GBP =", data["rates"]["GBP"])