from luno_python.client import Client

#App function

def CryptoBalance(picker):
    json_data = data.get_balances()
    if picker == 1:        
        coin = json_data['balance'][0]['balance']
        print('Your ethereum balance is :', coin, 'ETH')
    elif picker == 2:
        coin = json_data['balance'][2]['balance']
        print('Your bitcoin balance is :', coin, 'BTC')
    elif picker == 3:
        coin = json_data['balance'][3]['balance']
        print('Your ripple balance is :', coin, 'XRP')

#Authorization with the Luno API
user_credentials = {}                  #Allow user prompt only if theres no data

if user_credentials == {} :
    
    print('NOTE : If you do not have a Luno API key or API Key Secret, ')
    print('please signup for a Luno Account and get Luno API credentials from https://www.luno.com/wallet/security/api_keys')
    input('Press ENTER to continue')
    api_id = input('Please enter your API key here')
    api_secret = input('Please enter your API key secret here')
    user_credentials['api_id'] = api_id
    user_credentials['api_secret'] = api_secret

data = Client(api_key_id= user_credentials['api_id'] , api_key_secret= user_credentials['api_secret'])

#Permissions
Perm_R_Balance = 1

#Main Screen
do_something = int(input('Press 1 for crypto balance: '))

#Balance Checker
if do_something == 1:
    while True:
        picker = int(input('Press 1 for Ethereum, Press 2 for Bitcoin , Press 3 for Ripple'))
        if picker < 4:
            CryptoBalance(picker)
        else:
            break
        
