resaux = {"victor" : ["amine", "ambroise", "alexis"],
          "amine" : ["victor", "alexis", "ambroise"],
          "ambroise" : ["victor", "amine", "alexis", "florian"],
          "alexis" : ["amine"],
          "dimitri" : ["lukas", "alexis"],
          "florian" : ["alexis", "victor", "dimitri"],
          "lukas" : ["dimitri"]}

resaux2 = {"victor" : ["amine", "ambroise", "alexis"],
          "amine" : ["victor", "alexis", "ambroise"],
          "ambroise" : ["victor", "amine", "alexis", "florian"],
          "alexis" : ["amine", "leopold", "jad"],
          "dimitri" : ["leopold", "alexis"],
          "florian" : ["alexis", "victor", "dimitri"],
          "lukas" : ["dimitri", "jad"],
          "leopold" : ["ambroise", "amine", "rayan"],
          "rayan" : ["leopold", "jihed"],
          "jihed":["amine", "ambroise"],
          "jad" : ["lukas", "dimitri", "matheo"],
          "matheo" : ["jad","dimitri"]}

def algorithmeGlouton(liens, start, end) :
    deja_fait = []
    impasse = ""
    while end not in liens[start] :

        print("le nom utilisÃ© est :", start, deja_fait)

        if start in deja_fait :
            impasse = start
            start = liens[start][-1]

        if start == impasse :
            break

        else :
            for i2 in range(len(liens[start])) :

                #print("i2 : ", i2, "\n")

                if liens[start][i2] not in deja_fait :
                    print(liens[start][i2] not in deja_fait, " est le teste \n")
                    start = liens[start][i2]
                    break

        deja_fait.append(start)

    deja_fait.append(start)
    print(deja_fait)
    print(len(deja_fait))

def algoTraditionnel(liens, start, end) :
    memoire_vive = [start]
    memoire_morte = []
    found = False
    noeud = 0
    while not found :
        for i in range(len(memoire_vive)) :
            if end == memoire_vive[i] :
                found = True

        if not found :
            memoire_morte.extend(memoire_vive.copy())

            taille = len(memoire_vive)
            memoire_vive = []
            for i in range(taille) :

                for i2 in range(len(liens[memoire_morte[i-taille]])) :

                    memoire_vive.append(liens[memoire_morte[i-taille]][i2])

            memoire_morte.append("###new operation###")
            indice = 0
            while indice != len(memoire_vive) :
                while memoire_vive.count(memoire_vive[indice]) != 1 :
                    memoire_vive.remove(memoire_vive[indice])
                indice+=1
            noeud += 1
    print(memoire_morte)
    print(noeud)

personne_start = "dimitri"
personne_end = "victor"
algorithmeGlouton(resaux2, personne_start, personne_end)
algoTraditionnel(resaux2,personne_start, personne_end)