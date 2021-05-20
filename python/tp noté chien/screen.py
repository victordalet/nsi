import sys
def display(animal):
    """
    affiche les valeur du dictionnaire de l'animale
    animal : dictionnaire
    """
    for name, valeur in animal.items(): # boucle contenant deux variables pour le nom et la valeur de chaque clef dans le dictionaire
        print("donnée de votre animal: {} : {}".format(name,valeur))

def displayExiste(existe):
    """
    affiche l'existance de l'animal du client
    """
    if existe == True: # s'il existe
        print("votre chien existe")
    else: # s'il n'existe pas
        print("votre chien n'existe pas")
        sys.exit() # on femre le programme