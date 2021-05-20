# sujet B Dalet Victor 1e3
import json
from sauvegarde import *
from demande import *
from screen import *
from travail_dic import *


def main():
    """
    la fonction qui va appeller tous les autres fonctions
    """
    animal={"nom":"Rex","espece":"chien","nbr_pattes":4,"famille":"canides"} # au cas ou il y a un proble de charge json
    animal = chargeSaves()
    nom_animal =  firstQuestion()
    existe = comparaison(animal,nom_animal)
    displayExiste(existe)
    tatouage = demandeTatoue()
    rajoutDictionnaire(animal,tatouage)
    display(animal)
    saves(animal)

main()