import requests

url = 'https://prime.exchangerate-api.com/v5/4c9d7a2d30d56d42d0bd5d28/latest/MYR'

request = requests.get(url)
data = request.json()


# myr = data['conversion_rates']['MYR'] #Malaysian Ringgit
# aed = data['conversion_rates']['AED'] #United Arab Emirates Dirham
# ars = data['conversion_rates']['ARS'] #Argentine Peso
# aud = data['conversion_rates']['AUD'] #Australian Dollar
# bgn = data['conversion_rates']['BGN'] #Bulgarian Lev
# brl = data['conversion_rates']['BRL'] #Brazilian Real
# bsd = data['conversion_rates']['BSD'] #Bahamian Dollar
# cad = data['conversion_rates']['CAD'] #Canadian Dollar
# chf = data['conversion_rates']['CHF'] #Swiss Franc
# clp = data['conversion_rates']['CLP'] #Chilean Peso
# cny = data['conversion_rates']['CNY'] #Chinese Yuan
# cop = data['conversion_rates']['COP'] #Colombian Peso
# czk = data['conversion_rates']['CZK'] #Czech Koruna
# dkk = data['conversion_rates']['DKK'] #Danish Krone
# dop = data['conversion_rates']['DOP'] #Dominican Peso
# egp = data['conversion_rates']['EGP'] #Egyptian Pound
# eur = data['conversion_rates']['EUR'] #European Euro
# fjd = data['conversion_rates']['FJD'] #Fijian Dollar
# gbp = data['conversion_rates']['GBP'] #British Pound
# gtq = data['conversion_rates']['GTQ'] #Guatemalan Quetzal
# hkd = data['conversion_rates']['HKD'] #Hong Kong Dollar
# hrk = data['conversion_rates']['HRK'] #Croatian Kuna
# huf = data['conversion_rates']['HUF'] #Hungarian Forint
# idr = data['conversion_rates']['IDR'] #Indonesian Rupiah
# ils = data['conversion_rates']['ILS'] #Israeli New Shekel
# inr = data['conversion_rates']['INR'] #Indian Rupee
# isk = data['conversion_rates']['ISK'] #Icelandic Króna
# jpy = data['conversion_rates']['JPY'] #Japanese Yen
# krw = data['conversion_rates']['KRW'] #South Korean won
# kzt = data['conversion_rates']['KZT'] #Kazakhstani Tenge
# mxn = data['conversion_rates']['MXN'] #Mexican Peso
# nok = data['conversion_rates']['NOK'] #Norwegian Krone
# nzd = data['conversion_rates']['NZD'] #New Zealand Dollar
# pab = data['conversion_rates']['PAB'] #Panamanian Balboa
# pen = data['conversion_rates']['PEN'] #Peruvian Sol
# php = data['conversion_rates']['PHP'] #Philippine peso
# pkr = data['conversion_rates']['PKR'] #Pakistani Rupee
# pln = data['conversion_rates']['PLN'] #Poland złoty
# pyg = data['conversion_rates']['PYG'] #Paraguayan Guarani
# ron = data['conversion_rates']['RON'] #Romanian Leu
# rub = data['conversion_rates']['RUB'] #Russian Ruble
# sar = data['conversion_rates']['SAR'] #Saudi Riyal
# sek = data['conversion_rates']['SEK'] #Swedish Krona
# sgd = data['conversion_rates']['SGD'] #Singapore Dollar
# thb = data['conversion_rates']['THB'] #Thailand Baht
# tr = data['conversion_rates']['TRY'] #Turkish lira
# twd = data['conversion_rates']['TWD'] #New Taiwan Dollar
# uah = data['conversion_rates']['UAH'] #Ukrainian hryvnia
# usd = data['conversion_rates']['USD'] #United States Dollar
# uyu = data['conversion_rates']['UYU'] #Uruguayan Peso
# zar = data['conversion_rates']['ZAR'] #South African Rand


currencies = ['MYR', 'AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'KZT', 'MXN', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'UAH', 'USD', 'UYU', 'ZAR']
currencyDict = {}
for i in currencies:
    currencyDict[i] = data['conversion_rates'][i]

print(currencyDict)