from demande import first,askWord
from display import displayWord
from recherche import findWordInDict,findWordInDict2
from saves import openSave,savesName
from modification import rajout,supprimer
import json
dictionnaire = openSave()


def main():
    choix = 0
    while choix != 4:
        choix = first()
        if choix == 1:
            mot_demander = askWord(dictionnaire)
            mot_traduit = findWordInDict(mot_demander,dictionnaire)
            displayWord(mot_demander,mot_traduit)
        elif choix == 2:
            mot_demander = askWord(dictionnaire)
            mot_traduit = findWordInDict2(mot_demander,dictionnaire)
            displayWord(mot_demander,mot_traduit)
        elif choix == 3:
            rajout(dictionnaire)
            savesName(dictionnaire)
        elif choix == 5:
            supprimer(dictionnaire)
            savesName(dictionnaire)
        elif choix == 4 :
            print("aurevoir")
        else :
            print("cette demande n'existe pas")

main()