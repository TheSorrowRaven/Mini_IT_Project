import requests

url = 'https://prime.exchangerate-api.com/v5/4c9d7a2d30d56d42d0bd5d28/latest/MYR'

request = requests.get(url)
data = request.json()

myr = data['conversion_rates'][0] #Malaysian Ringgit
aed = data['conversion_rates'][1] #United Arab Emirates Dirham
ars = data['conversion_rates'][2] #Argentine Peso
aud = data['conversion_rates'][3] #Australian Dollar
bgn = data['conversion_rates'][4] #Bulgarian Lev
brl = data['conversion_rates'][5] #Brazilian Real
bsd = data['conversion_rates'][6] #Bahamian Dollar
cad = data['conversion_rates'][7] #Canadian Dollar
chf = data['conversion_rates'][8] #Swiss Franc
clp = data['conversion_rates'][9] #Chilean Peso
cny = data['conversion_rates'][10] #Chinese Yuan
cop = data['conversion_rates'][11] #Colombian Peso
czk = data['conversion_rates'][12] #Czech Koruna
dkk = data['conversion_rates'][13]
dop = data['conversion_rates'][14]
egp = data['conversion_rates'][15]
eur = data['conversion_rates'][16]
fjd = data['conversion_rates'][17]
gbp = data['conversion_rates'][18]
gtq = data['conversion_rates'][19]
hkd = data['conversion_rates'][20]
hrk = data['conversion_rates'][21]
huf = data['conversion_rates'][22]
idr = data['conversion_rates'][23]
ils = data['conversion_rates'][24]
inr = data['conversion_rates'][25]
isk = data['conversion_rates'][26]
jpy = data['conversion_rates'][27]
krw = data['conversion_rates'][28]
kzt = data['conversion_rates'][29]
mxn = data['conversion_rates'][30]
nok = data['conversion_rates'][31]
nzd = data['conversion_rates'][32]
pab = data['conversion_rates'][33]
pen = data['conversion_rates'][34]
php = data['conversion_rates'][35]
pkp = data['conversion_rates'][36]
pln = data['conversion_rates'][37]
pyg = data['conversion_rates'][38]
ron = data['conversion_rates'][39]
rub = data['conversion_rates'][40]
sar = data['conversion_rates'][41]
sek = data['conversion_rates'][42]
sgd = data['conversion_rates'][43]
thb = data['conversion_rates'][44]
tr = data['conversion_rates'][45] #try
twd = data['conversion_rates'][46]
uah = data['conversion_rates'][47]
usd = data['conversion_rates'][48]
uyu = data['conversion_rates'][49]
zar = data['conversion_rates'][50]

print(data)