def displayWord(mot_demander,mot_traduit):
    if mot_traduit == False:
        print("le mot n'existe pas")
    else:
        for nombre in range(len(mot_traduit)):
            print("le mot {} se dit {}".format(mot_demander,mot_traduit[nombre]))
