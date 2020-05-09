# Naga
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


def PriceTicket(picker):
    json_data = data.get_tickers()
    if picker == 1:        
        price = json_data['tickers'][1]['ask']
        print('The current ethereum price is : RM', price)
        return price

    elif picker == 2:
        price = json_data['tickers'][3]['ask']
        print('The current bitcoin price is : RM', price)
        return price

    elif picker == 3:
        price = json_data['tickers'][14]['ask']
        print('The current ripple price is : RM', price)
        return price

def BuyCoins(picker):

        if picker == 1:
            buyvalue = float(input('Enter the amount of ethereum you want to buy: '))
            print('The following will be {} ETH').format(PriceTicket(1) * buyvalue)
            option = input('Would you like to confirm your transaction? (Y/N) :')
            if option == "Y":
                data.create_quote(buyvalue, 'ETHMYR', 'BUY')
            elif option == "N":
                pass
            else:
                print('Wrong input , please try again')

        elif picker == 2:
            buyvalue = float(input('Enter the amount of bitcoin you want to buy: '))
            print('The following will be {} BTC').format(PriceTicket(2) * buyvalue)
            option = input('Would you like to confirm your transaction? (Y/N) :')
            if option == "Y":
                data.create_quote(buyvalue, 'XBTMYR', 'BUY')
            elif option == "N":
                pass
            else:
                print('Wrong input, please try again')

        elif picker == 3:
            buyvalue = float(input('Enter the amount of ripple you want to buy: '))
            print('The following will be {} XRP').format(PriceTicket(3) * buyvalue)
            option = input('Would you like to confirm your transaction? (Y/N) :')
            if option == "Y":
                data.create_quote(buyvalue, 'XRPMYR', 'BUY')
            elif option == "N":
                pass
            else:
                print('Wrong input , please try again')


        else:
            print('Invalid input, please try again')

def SellCoins(picker):

        if picker == 1:
            sellvalue = float(input('Enter the amount of ethereum you want to sell: '))
            print('The following will be RM {}').format(PriceTicket(1) / sellvalue)
            option = input('Would you like to confirm your transaction? (Y/N) :')
            if option == "Y":
                data.create_quote(sellvalue, 'ETHMYR', 'BUY')
            elif option == "N":
                pass
            else:
                print('Wrong input , please try again')

        elif picker == 2:
            sellvalue = float(input('Enter the amount of bitcoin you want to buy: '))
            print('The following will be RM {}').format(PriceTicket(2) * sellvalue)
            option = input('Would you like to confirm your transaction? (Y/N) :')
            if option == "Y":
                data.create_quote(sellvalue, 'XBTMYR', 'BUY')
            elif option == "N":
                pass
            else:
                print('Wrong input, please try again')

        elif picker == 3:
            sellvalue = float(input('Enter the amount of ripple you want to buy: '))
            print('The following will be RM {}').format(PriceTicket(3) * sellvalue)
            option = input('Would you like to confirm your transaction? (Y/N) :')
            if option == "Y":
                data.create_quote(sellvalue, 'XRPMYR', 'BUY')
            elif option == "N":
                pass
            else:
                print('Wrong input , please try again')

def CreateAccount(picker):

    if picker == 1:
        name = input('Enter Name')
        json_data = data.create_account('ETH', name)
        print(json_data)

    elif picker == 2:
        name = input('Enter Name')
        json_data = data.create_account('BTC', name)
        print(json_data)

    elif picker == 3:
        name = input('Enter Name')
        json_data = data.create_account('XRP', name)
        print(json_data)



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

#Main Screen
do_something = int(input('Press 1 for crypto balance, press 2 for crypto prices, press 3 to buy coins: '))

#Balance Checker
while True:
    if do_something == 1:
        picker = int(input('Press 1 for Ethereum, Press 2 for Bitcoin , Press 3 for Ripple: '))
        if picker < 4:
             CryptoBalance(picker)
        else:
            break

#Crypto prices
    elif do_something == 2:
        picker = int(input('Press 1 for Ethereum, Press 2 for Bitcoin , Press 3 for Ripple: '))
        if picker < 4:
            PriceTicket(picker)
        else:
            break

    elif do_something == 3:
        picker = int(input('Press 1 for Ethereum, Press 2 for Bitcoin , Press 3 for Ripple: '))
        if picker < 4:
            BuyCoins(picker)

    elif do_something == 4:
            picker = int(input('Press 1 for BTC, press 2 for ETH , press 3 for BTC'))
            CreateAccount(picker)
            
 

    
        
