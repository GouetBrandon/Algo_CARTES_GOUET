class Carte:
    def __init__ (self,name,manaCost,description):
        self.__name=name
        self.__manaCost=manaCost
        self.__description=description

    def getName (self):
        return self.__name

    def getManaCost (self):
        return self.__manaCost

    def getDescription (self):
        return self.__description