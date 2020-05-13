###
#/***************************************************
#File Name: constants.py
#Version/Date: 1.0 (2020-05-13)
#Programmer/ID: Raven Lim Zhe Xuan (1191101213)
#Project Name: Smart Finance Manager 
#Teammates: Nagaindran A/L Kanaseelanayagam, Raja Muhammad Darwisy bin Raja Ahmad, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###



# Save File Location/Name
saveFile = "PICKLE.RICKKK"

# Window Names
mainWindow    = "Main"
warningWindow = "Warning"
queryWindow   = "Query"

# Main Window Base
mainDisplayTitle   = "Smart Financial Planner"
mainWindowSize     = "1280x720"
mainWindowBgColor  = "white"
mainWindowAltColor = "#ABABAB"

# Warning Window Base
warningDisplayTitle  = "Warning"
warningWindowSize    = "350x150"
warningWindowBgColor = "gray"

# Query Window Base
queryDisplayTitle  = "Query"
queryWindowSize    = "500x250"
queryWindowBgColor = "gray"

# Navigation Bar
navBarColor = "#eeeeee"

# Subwindow Names
mainMenuSub   = "MainMenuSub"
plannerSub    = "PlannerSub"
accountSub    = "AccountSub"
investmentSub = "InvestmentSub"

# MainMenu Sub
firstButtonYVal = 275
nextButtonYDiff = 115

# Exceptions
switchLenException = "Commands List' len() must have +1 default state than Constants List len()"


if __name__ == "__main__":
    print("Please run main.py instead")
    pass
