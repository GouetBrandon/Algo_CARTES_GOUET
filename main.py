from carte import Carte
from mage import Mage
from cristal import Cristal
from creature import Creature
from blast import Blast

gobelin=Creature(20,10,"Gobelin",10,"Un gros Gobelin bien dégueu")
loup=Creature(10,20,"Loup",10,"Un ptit loup tout mignon")
golem=Creature(50,30,"Golem",30,"Bim Bam Boum fait le golem")

petitCristal=Cristal(5,"petit Cristal",0,"Un petit cristal de mana")
grosCristal=Cristal(10,"Gros Cristal",5,"Un gros Cristal")

petitBlast=Blast(5,"petit Blast",5,"une petite explosion")
grosBlast=Blast(15,"Gros Blast",15,"Une grosse explosion")

playerMain=[loup,gobelin,golem,petitCristal,grosCristal,petitBlast,grosBlast]
playerDefausse=None
playerZoneDeJeu=None
ennemiMain=[loup,gobelin,golem,petitCristal,grosCristal,petitBlast,grosBlast]
ennemiDefausse=None
ennemiZoneDeJeu=None

print("Veuillez choisir un nom pour votre mage")
playerName=str(input())

player1=Mage(playerName,100,100,100,playerMain,playerDefausse,playerZoneDeJeu)
ennemi=Mage("Yo Gah Ho",100,100,100,ennemiMain,ennemiDefausse,ennemiZoneDeJeu)

print("Bienvenue sur StoneHeart ! Le combat va bientôt commencer !")
input("...")
print("Il opposera ",player1.getName()," à ", ennemi.getName()," !")
input("...")
print("Que le combat commence !")
input("...")

#while player1.getPV() != 0 or ennemi.getPV() != 0:
print("PV: ",player1.getPV()," |  Mana: ",player1.getActualMana(),"/",player1.getTotalMana())
print("Veuillez Choisir une carte dans votre main à placer dans la zone de jeu")
print("Main :")
for i in range(len(playerMain)):
    print(playerMain[i].getName())

print("-----------------------------------------")

playerChoice =str(input())

if playerChoice == "Loup":

    print("vous invoquer un loup !")
    input()
    print("PV: ",player1.getPV()," |  Mana: ",player1.getActualMana(),"/",player1.getTotalMana())
    player1.setActualMana(-10)