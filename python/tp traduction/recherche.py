def findWordInDict(mot_demander,dictionnaire):
    try:
        mot_traduit = []
        for name,value in dictionnaire.items():
            print(dictionnaire)
            if mot_demander == name:
                mot_traduit.append(value)
        return mot_traduit
    except:
        mot_traduit = False
        return mot_traduit

def findWordInDict2(mot_demander,dictionnaire):
    try:
        mot_traduit = []
        for name,value in dictionnaire.items():
            if mot_demander == value:
                mot_traduit.append(name)
        return mot_traduit
    except:
        mot_traduit = False
        return mot_traduit



