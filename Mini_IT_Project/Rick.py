# Raven

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

