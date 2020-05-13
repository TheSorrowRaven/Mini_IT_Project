###
#/***************************************************
#File Name: interfaces.py
#Version/Date: 1.0 (2020-05-13)
#Programmer/ID: Raven Lim Zhe Xuan (1191101213)
#Project Name: Smart Finance Manager 
#Teammates: Nagaindran A/L Kanaseelanayagam, Raja Muhammad Darwisy bin Raja Ahmad, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###



class IOnSave():
    def __init__(self, main):
        main.AddSaveEvent(self)
    def OnSave(self):
        pass

class IOnLoad():
    def OnLoad(self, main):
        main.AddLoadEvent(self)
        pass

    
if __name__ == "__main__":
    print("Please run main.py instead")
    pass
