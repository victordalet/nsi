def rajoutDictionnaire(animal,tatouage):
    """
    rajoute la valeur  du tatouge dans le dictionnaire initiale
    animal : dictionnaire
    tatouage : bouléens
    """
    animal.update({"tatouage":tatouage}) # rajoute le non tatouage à la valeur d'un bouléen


def comparaison(animal,nom_animal):
    """
    Compare dans le fichier les nom d'animal pour retrouver celuio de l'utilisateur
    animal : dictionnaire
    nom_animal : str
    retrun bouléen
    """
    try :  # si la valeur existe
        if animal["nom"] == nom_animal: # si le nom du chien est celui de l'utilisateur
                return True
    except:
        return False