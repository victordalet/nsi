import math
#On demande la limite
liste=[]
limite=int(input("Rechercher un nombre premier jusqu'à ?"))
#On parcourt les entiers de 1 jusq'à cette limite
for nbr in range(2,limite+1):
    #On considère qu'il est premier
    est_premier=True;
    #On parcourt les entiers de 2 jusqu'à la racine du nombre en cours
    for diviseur in range(2,int(math.sqrt(nbr))+1):
        #Si on detecte un diviseur, le nombre n'est plus premier
        if nbr % diviseur == 0 :
            est_premier=False
            break;
    #Affichage selon la primalité
    if est_premier==True :
        liste.append(nbr)
print(liste)



