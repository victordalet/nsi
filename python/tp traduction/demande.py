def first():
    choix = int(input("1 = Francais-Anglais ; 2= Anglais-Francais ; 3 = rajouter/modifier ; 4=stop  5 = supprimer " ))
    return choix

def askWord(dictionnaire):
   mot_demnader = input("choisisser un mot")
   return mot_demnader.lower()