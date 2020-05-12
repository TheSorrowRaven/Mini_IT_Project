# Raven



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
