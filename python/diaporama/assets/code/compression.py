phrase  = "salut comment tu va ?".encode()
"La phrase « this is an example of a huffman tree » se code alors sur 135 bits au lieu de 288 bits (si le codage initial des caractères tient sur 8 bits). "
liste = []

def algoTrad():
    """
    transforme la phrase en binaire
    :return:
    """
    for i in phrase: # parcoure la phrase
        liste.append(bin(i)) # rajoute le code binaire du caratère dans une liste
    print("trad : ",liste) # affiche la liste pleine

def algoGlouton():
    """
    transforme la phrase en binaire en optimisant
    :return:
    """
    liste_code = [] # variable pour une liste contenant les lettres codé par odre décroissant
    phrase_mix = list(phrase.decode()) # la phrase initiale mit en liste pour la décomposé
    while phrase_mix != []: # tant que la phrase n'est pas lu en entier
        lettre_max = ["",0] # valeur de départ pour trouvé la lettre la plus grande
        for ele in phrase_mix: # boucle pour parcourir la phrase en liste
            if phrase_mix.count(ele) > lettre_max[1]: # detecte quand l'un des chiffres est le plus grands
                lettre_max = [ele,phrase_mix.count(ele)]
        for i in str(lettre_max[0]).encode():
            liste_code.append(bin(i)) # pour le mettre en binaire dans la liste
        for i in range(lettre_max[1]): # tant que la lettre existe
            phrase_mix.remove(lettre_max[0]) # on l'enleve de la phrase pour pouvoir passer au suivant

    for lettre in phrase: # on parcoure la phrase initiale
        lettre_bin = bin(lettre)  # on convertie chaque lettre
        liste.append(bin(liste_code.index(lettre_bin))) # on regarde quelle est sa position dans la liste et on la sauvegarde en binaire
    print("glouton : ",liste,)

algoTrad()
liste=[]
algoGlouton()