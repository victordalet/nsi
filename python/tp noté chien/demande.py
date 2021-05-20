def firstQuestion():
    """
    demande à l'utilisateur qu'elle est le nom de son animal
    return : le nom de l'animal
    """
    nom_animal = input("quelle est le nom de votre animal ?")
    return nom_animal

def demandeTatoue():
    """
    Permet de demander à l'utilisateur si son chien est tatoué
    renvoie True ou False selon son choix
    """
    while 42: #boucle permettant à l'utilisateur de retaper sa demande s'il ne met pas oui ou non
        tatouage = input("votre animal est-il tatoué ? (oui ou non)") # demande de l'utilisateur
        if tatouage == "oui": # si le chien est tatoué
            return True
        elif tatouage == "non": # s'il ne l'est pas
            return False