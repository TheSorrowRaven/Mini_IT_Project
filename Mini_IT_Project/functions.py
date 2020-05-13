###
#/***************************************************
#File Name: account.py
#Version/Date: 1.0 (2020-05-13)
#Programmer/ID: Raven Lim Zhe Xuan (1191101213)
#Project Name: Smart Finance Manager 
#Teammates: Nagaindran A/L Kanaseelanayagam, Raja Muhammad Darwisy bin Raja Ahmad, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###

import constants as Constants

class Switch:

    def __init__(self, constantsList: list, commandsList: list, targetValue):
        if (len(constantsList) != (len(commandsList) - 1)):
            raise Exception(Constants.switchLenException)   # Code will end if this occurs

        if targetValue in constantsList:
            commandsList[constantsList.index(targetValue)]()
        else:
            commandsList[len(commandsList) - 1]()


if __name__ == "__main__":
    print("Please run main.py instead")
    pass
