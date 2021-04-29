def detecterDoublons(prenoms):
    """
    Renvoie True s'il y a des doublons dans la liste
    :param prenoms:
    :return:
    """
    for i in prenoms:
        presence_doublons = prenoms.count(i)
        if presence_doublons:
            return True

    return  False


def enleverDoublons(prenoms):
    """
    retire les doublons dans une autre liste
    :param prenoms:
    :return:
    """
    nouvelle_liste = []
    for i in prenoms:
        if i not in nouvelle_liste:
            nouvelle_liste.append(i)
    return nouvelle_liste