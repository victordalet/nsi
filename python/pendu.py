import random
liste_mots=["chat","chien","maison","rapace","juif","argent"] # liste des mots
liste_lettre=[] # liste a completter
tours = 0
win =False
def chooseWord(liste_mots):
 """ Cette fonction choisit au hasard un mot dans une liste
        de mots prédéfinie (en haut du programme)
        Entree : la liste de mots (list)
        Sortie : le mot choisi (string)"""
 mot =random.choice(liste_mots)
 return mot

def askLetter(liste_lettre):
    """ Demande à l'utilisateur de taper une lettre.
        Entree : /
        Sortie : la lettre tapee (string)
        """
    lettre = input("choissiser une lettre")

    return lettre
def cheak(lettre,mot):
     """Vérifie si la lettre envoyée en parametre est dans le mot
        envoyé en parametre
        Entrées : la lettre, et le mot
        Sortie : booléen"""
     if lettre in  mot :
       if win == False:
        liste_lettre.append(lettre)
        print("{lettre} est la bonne lettre".format(lettre=lettre))
        print("lettre trouvé: {liste_lettre}".format(liste_lettre=liste_lettre))

     else:
         print ("{lettre} n'est pas la bonne lettre".format(lettre=lettre))
         print("lettre trouvé: {liste_lettre}".format(liste_lettre=liste_lettre))
def found(mot,lettre):
    """Détermine si le mot a été trouvé ou pas.
        Entrée : liste des lettres trouvées,mot à chercher
        Sortie : booléen
        """
    if mot == lettre:
        return True
    return False
def gameLost(win,lettre,reponse,tours,mot):
    """Détermine si le jeu est perdu ou pas. Le jeu est perdu si plus de x questions
ont été posées
		"""
    tours += 1
    if tours == 10:
        print("perdu, le mot était {mot}".format(mot=mot))
    elif win == True :
        print("vous avez gagnée au bout de {tours} tours".format(tours=tours))
    else:
        print("vous êtes aux {tours} tours".format(tours=tours))
    return tours

mot = chooseWord(liste_mots)
while win == False :
    lettre = askLetter(liste_lettre)
    reponse = cheak(lettre,mot)
    win = found(mot,lettre)
    tours = gameLost(win,lettre,reponse,tours,mot)


