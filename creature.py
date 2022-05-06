from carte import Carte

class Creature(Carte):
    def __init__ (self,pv,attack,name,manaCost,description):
        Carte.__init__ (self,name,manaCost,description)
        self.__pv=pv
        self.__attack=attack


    def getPV (self):
        return self.__pv

    def setPV (self,valeur):
        self.__pv=self.__pv + valeur
        if self.__pv < 0:
            self.__pv = 0
        return self.__pv

    def hasAttack (self,hasAttack):
        if hasAttack == False:
            hasAttack == True
        else :
            hasAttack == False