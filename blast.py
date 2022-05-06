from carte import Carte

class Blast(Carte):
    def __init__ (self,valeur,name,manaCost,description):
        Carte.__init__ (self,name,manaCost,description)
        self.__valeur=valeur

    def getValeur (self):
        return self.__valeur