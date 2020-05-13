#/***************************************************
#File Name: bankbalance.py
#Version/Date: 0.5 (2020-05-06)
#Programmer/ID: Fong Zheng Wei (1191100350)
#Project Name: Smart Finance Manager 
#Teammates: Raven Lim Zhe Xuan, Raja Muhammad Darwisy bin Raja Ahmad, Nagaindran A/L Kanaseelanayagam
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###


""" 
███████ ██       █████   ██████   ██████  ███████ ██████                                                       
██      ██      ██   ██ ██       ██       ██      ██   ██                                                      
█████   ██      ███████ ██   ███ ██   ███ █████   ██   ██                                                      
██      ██      ██   ██ ██    ██ ██    ██ ██      ██   ██                                                      
██      ███████ ██   ██  ██████   ██████  ███████ ██████                                                       
                                                                                                               
                                                                                                               
███    ██  ██████  ████████     ██ ███    ██  ██████ ██      ██    ██ ██████  ███████ ██████      ██ ███    ██ 
████   ██ ██    ██    ██        ██ ████   ██ ██      ██      ██    ██ ██   ██ ██      ██   ██     ██ ████   ██ 
██ ██  ██ ██    ██    ██        ██ ██ ██  ██ ██      ██      ██    ██ ██   ██ █████   ██   ██     ██ ██ ██  ██ 
██  ██ ██ ██    ██    ██        ██ ██  ██ ██ ██      ██      ██    ██ ██   ██ ██      ██   ██     ██ ██  ██ ██ 
██   ████  ██████     ██        ██ ██   ████  ██████ ███████  ██████  ██████  ███████ ██████      ██ ██   ████ 
                                                                                                               
                                                                                                               
███    ███  █████  ██ ███    ██     ██████  ██████   ██████   ██████  ██████   █████  ███    ███               
████  ████ ██   ██ ██ ████   ██     ██   ██ ██   ██ ██    ██ ██       ██   ██ ██   ██ ████  ████               
██ ████ ██ ███████ ██ ██ ██  ██     ██████  ██████  ██    ██ ██   ███ ██████  ███████ ██ ████ ██               
██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██  ██  ██               
██      ██ ██   ██ ██ ██   ████     ██      ██   ██  ██████   ██████  ██   ██ ██   ██ ██      ██               
                                                                                                               
                                                                                                            
 """


class BankAccount():

    def __init__(self): # When BankAccount is created, this will be instantly called
        self.amount = 0 # Upon creation, their money is set to 0

    def DepositMoney(self, money):
        self.amount = self.amount + money

    def WithdrawMoney(self, money):
        self.amount = self.amount - money

#over here is out of class, note indentation



myAcc = BankAccount()   # Object creation

myAcc.DepositMoney(20)      #So myAcc got 20 money

fongsAcc = BankAccount()  # Object creation

fongsAcc.DepositMoney(100)    #Add money to Fong Account

fongsAcc.WithdrawMoney(10) #Taxes

print(myAcc.amount)
print(fongsAcc.amount)