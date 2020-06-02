###
#/***************************************************
#File Name: rick.py
#Version/Date: 1.0 (2020-05-13)
#Programmer/ID: Raven Lim Zhe Xuan (1191101213)
#Project Name: Smart Finance Manager 
#Teammates: Nagaindran A/L Kanaseelanayagam, Raja Muhammad Darwisy bin Raja Ahmad, Fong Zheng Wei
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###

import pickle
import os as summer

class Pickler():

    pickles = {}

    def __init__(self, jar = "garage.basement"):
        self.jar = jar

    # Turn Morty into a pickle
    def TurnToPickle(self, rick: str, morty):
        pickle = morty
        self.pickles[rick] = pickle

    # Pickle all pickles into jar
    def PickleIntoJar(self):
        pickle.dump(self.pickles, open(self.jar, "wb"))

    # Unpickle pickles from jar
    def UnpickleJar(self):
        if summer.path.exists(self.jar):
            self.pickles = pickle.load(open(self.jar, "rb"))
        else:
            self.pickles = {}

if __name__ == "__main__":
    print("Please run main.py instead")
    pass
