import json
def chargeSaves():
    """
    recupère la sauvegarde de l'utilisateur
    return : dictionnaire
    """
    fp = open('data.json') # on charge le fichier
    animal = json.load(fp) # on recupère notre dictionnaire
    return animal



def saves(animal):
    """
    sauvegarde le dictionnaire de l'utilisateur
    animal : dictionnaire
    """
    with open("data.json","w") as fp: # on ouvre ou creer un fichier json en mode w pour pouvoir modifier le fichier
        json.dump(animal,fp) # on sauvegarde le dictionnaire
    print("sauvegarde effectué")