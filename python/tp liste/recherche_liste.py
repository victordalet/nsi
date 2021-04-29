def afficherInitial(prenoms):
    """
    Permet d'afficher l'initial de chaque element de la liste
    :param prenoms:
    :return:
    """
    for i in prenoms:
        print(i[0])

def prenomSuperieure(prenoms):
    """
    detecte le prénom fait le plus de fois
    :param prenoms:
    :return:
    """
    prenoms_max = ["",0]
    for ele in prenoms:
        if prenoms.count(ele) > prenoms_max[1]:
            print(prenoms.count(ele))
            prenoms_max = [ele,prenoms.count(ele)]
    return prenoms_max
