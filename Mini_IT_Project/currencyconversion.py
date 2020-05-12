# Naga
import requests

url = 'https://prime.exchangerate-api.com/v5/4c9d7a2d30d56d42d0bd5d28/latest/MYR'

request = requests.get(url)
data = request.json()

# Note MYR is the relative currency so MYR = 1 unit
currencies = ['MYR', 'AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'EGP', 
'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'KZT', 'MXN', 'NOK', 'NZD', 'PAB', 
'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'UAH', 'USD', 'UYU', 'ZAR']

currencyDict = {}
for i in currencies:
    currencyDict[i] = data['conversion_rates'][i]

def getRate(current: str, convertTo: str) -> float:
    return currencyDict[convertTo] / currencyDict[current]

def convert(current: str, convertTo: str, value: float) -> float:
    return value * getRate(current, convertTo)

# print(convert('AUD', 'MYR', 69))
# print(convert('USD', 'EGP', 420))


if __name__ == "__main__":
    print("Please run main.py instead")
    pass