class Mage:
    def __init__ (self,name,pv,totalMana,actualMana,main,defausse,zoneDeJeu):
        self.__name=name
        self.__pv=pv
        self.__totalMana=totalMana
        self.__actualMana=actualMana
        self.__main=main
        self.__defausse=defausse
        self.__zoneDeJeu=zoneDeJeu

    def getName (self):
        return self.__name

    def getPV (self):
        return self.__pv

    def setPV (self,valeur):
        self.__pv = self.__pv + valeur
        if self.__pv < 0:
            self.__pv = 0
        return self.__pv

    def getTotalMana (self):
        return self.__totalMana

    def getActualMana (self):
        return self.__actualMana

    def setActualMana (self,valeur):
        self.__actualMana = self.__actualMana + valeur
        if self.__actualMana < 0:
            self.__actualMana = 0
        return self.__actualMana

    def getMain (self):
        return self.__main

    def setMain (self,carte):
        self.__main.__append(carte)
        return self.__main

    def getDefausse (self):
        return self.__defausse

    def setDefausse (self,carte):
        self.__defausse.append(carte)
        return self.__defausse

    def getZoneDeJeu (self):
        return self.__zoneDeJeu

    def setZoneDeJeu (self,carte):
        self.__zoneDeJeu.append(carte)
        return self.__zoneDeJeu
