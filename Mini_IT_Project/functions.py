# Raven
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
