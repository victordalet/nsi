def rajout(dictionnaire):
    new_word_fr = input("mot francais")
    new_word_an = input("traduction anglais")
    dictionnaire.update({new_word_fr:new_word_an})

def supprimer(dictionnaire):
    langue_selectionner = input("quelle langue : 1=fr ; 2=an")
    mot_sup = input("quelle mot supprimer")
    dictionnaire.pop(mot_sup)