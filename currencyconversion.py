import requests

url = 'https://prime.exchangerate-api.com/v5/4c9d7a2d30d56d42d0bd5d28/latest/MYR'

request = requests.get(url)
data = request.json()

MYR = data['conversion_rates'][0] #Malaysian Ringgit
AED = data['conversion_rates'][1] #United Arab Emirates Dirham
ARS = data['conversion_rates'][2] #Argentine Peso
AUD = data['conversion_rates'][3] #Australian Dollar
BGN = data['conversion_rates'][4] #Bulgarian Lev
BRL = data['conversion_rates'][5] #Brazilian Real
BSD = data['conversion_rates'][6] #Bahamian Dollar
CAD = data['conversion_rates'][7] #Canadian Dollar
CHF = data['conversion_rates'][8] #Swiss Franc
CLP = data['conversion_rates'][9] #Chilean Peso
CNY = data['conversion_rates'][10] #Chinese Yuan
COP = data['conversion_rates'][11] #Colombian Peso
CZK = data['conversion_rates'][12] #Czech Koruna
DKK = data['conversion_rates'][13]
DOP = data['conversion_rates'][14]
EGP = data['conversion_rates'][15]
EUR = data['conversion_rates'][16]
FJD = data['conversion_rates'][17]
GBP = data['conversion_rates'][18]
GTQ = data['conversion_rates'][19]
HKD = data['conversion_rates'][20]
HRK = data['conversion_rates'][21]
HUF = data['conversion_rates'][22]
IDR = data['conversion_rates'][23]
ILS = data['conversion_rates'][24]
INR = data['conversion_rates'][25]
ISK = data['conversion_rates'][26]
JPY = data['conversion_rates'][27]
KRW = data['conversion_rates'][28]
KZT = data['conversion_rates'][29]
MXN = data['conversion_rates'][30]
NOK = data['conversion_rates'][31]
NZD = data['conversion_rates'][32]
PAB = data['conversion_rates'][33]
PEN = data['conversion_rates'][34]
PHP = data['conversion_rates'][35]
PKR = data['conversion_rates'][36]
PLN = data['conversion_rates'][37]
PYG = data['conversion_rates'][38]
RON = data['conversion_rates'][39]
RUB = data['conversion_rates'][40]
SAR = data['conversion_rates'][41]
SEK = data['conversion_rates'][42]
SGD = data['conversion_rates'][43]
THB = data['conversion_rates'][44]
TRY = data['conversion_rates'][45]
TWD = data['conversion_rates'][46]
UAH = data['conversion_rates'][47]
USD = data['conversion_rates'][48]
UYU = data['conversion_rates'][49]
ZAR = data['conversion_rates'][50]

print(data)