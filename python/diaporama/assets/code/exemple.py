billets = [5,1,30,29,11]
somme = 0
def algoGlouton(somme):
    """
    trouve le plus grand résultat d'une adition de trois nombre de la suite en cherchant le maw d'une liste
    :param somme:
    :return:
    """
    for temps in range(3): # boucle pour les 3 nombres
            somme += max(billets) # on récupère le plus grand nombre
            billets.remove(max(billets)) # on enleve le plus grand nombre de la liste afin de trouver le suivant
    print(somme)


def algoTrad():
    """
    trouve le plus grand résultat d'une adition de trois nombre de la suite en cherchant toutes les possibilitées
    :return:
    """
    somme_max = 0 # variable pour trouver la plus grande somme
    somme2 = 0 # variable pour le calcule
    for i in billets: # parcoure de la liste
        nombre1 =i # le premier nombre a additionner
        for i2 in billets:
            if i2!= nombre1: # le deuxième ne doit pas être égale au premier
                nombre2= i2
                for i3 in billets:
                    if i3 != nombre1 and i3 != nombre2:# le trisième ne doit pas être égale au premier et au deuxième
                        nombre3 = i3
                        somme2 = 0
                        somme2 = nombre1+nombre2+nombre3 # somme
                        if somme2 > somme_max: # si la somme trouvé est plus grande que la somme max trouvé auparavant
                            somme_max = somme2 # remplacer la valeur par la nouvelle plus grande

    print(somme_max)


algoGlouton(somme)
billets = [5,1,30,29,11]
somme = 0
algoTrad()

