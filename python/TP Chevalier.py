import random
import time

#Initialisation des points de vie
pv_chevalier=100;
pv_dragon=100;
nb_tour=1

def displayASCII():#Affichage d'un ASCII ART
 """
    affiche le chevalier

    """
 print(r"""
      __      _
     /__\__  //
    //_____\///
   _| /-_-\)|/_
  (___\ _ //___\
  (  |\\_/// * \\
   \_| \_((*   *))
   ( |__|_\\  *//
   (o/  _  \_*_/
   //\__|__/\
  // |  | |  |
 //  _\ | |___)
//  (___|
""")
def computeDragonDamages():
   """degats du dragon
   entrée : rien
   sortie: degats_dragon
   """
   degats_dragon=random.randint(0,10)
   return degats_dragon


def computeKnightDamages():
    """
    degats chevalier
    entrée= rien
    sortrie= degats_chevalier
    """
    degats_chevalier=random.randint(0,10)
    return degats_chevalier

def lives(degats_chevalier,degats_dragon,pv_chevalier,pv_dragon):
    """
nombre de pv
entré degats_dragon,degats_chevalier
sortie= pv_chevalier,pv_dragon
    """
    pv_chevalier=pv_chevalier-degats_dragon
    pv_dragon=pv_dragon-degats_chevalier
    return pv_chevalier,pv_dragon
def displayLives(pv_chevalier,pv_dragon):
    """
    vie des perso
    entréé:pv_chevalier,pv_dragon
    sortie:
    """
    time.sleep(1)
    print("point de vie du dragon {pv_dragon} point de vie du chevalier{pv_chevalier}".format(pv_dragon=pv_dragon,pv_chevalier=pv_chevalier))


def getWinner(pv_chevalier,pv_dragon):
    """
gere la win
entrée : pv_chevalier,pv_dragon
sortie: win
    """
    if pv_chevalier < 0:
        return "dragon"
    if pv_dragon < 0:
        return "chevalier"
    if pv_chevalier and pv_dragon <0:
        return"chevalier et dragon"

def displayWinner(win):
    """
message de gagnany
entrée:win
sortie=rien
    """
    print("le {win} a ganée".format(win=win))

def critique(pv_dragon):
 """
s'occupe des degats critique
entréé : pv_dragon
sortie : pv_dragon
 """
 chance= random.randint(0,100)
 if chance < 30:
  val1 = random.randint(1,20)
  val2 = random.randint(1,20)
  temps1 = round(time.time())
  calcule = int(input("combien font {val1} +  {val2}".format(val1=val1,val2=val2)))
  if calcule == val1 + val2:
   temps2 = round(time.time())
   if temps2 - temps1 <5:
    pv_dragon -=20
    print("coup critique ; -20 pour le dragon")
   else : print("dommage tu as pris trop de temps")
  else: print("dommage ce n'était pas la bonne réponse")
 return pv_dragon


displayASCII()
while pv_chevalier>0 and pv_dragon>0:
    degats_dragon=computeDragonDamages()
    degats_chevalier=computeKnightDamages()
    pv_chevalier,pv_dragon=lives(degats_chevalier,degats_dragon,pv_chevalier,pv_dragon)
    displayLives(pv_chevalier,pv_dragon)
    pv_dragon = critique(pv_dragon)

win=getWinner(pv_chevalier,pv_dragon)
displayWinner(win)

