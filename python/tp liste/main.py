from display import display
from doublons import detecterDoublons, enleverDoublons
from recherche_liste import afficherInitial, prenomSuperieure

prenoms = ["Sylvie","Charles","Alexis","Alexis","Vladimir","Hélène","Thomas","Sylvie","Alexis"]


def main():
    afficherInitial(prenoms)
    resultat = detecterDoublons(prenoms)
    nouvelle_liste = enleverDoublons(prenoms)
    prenoms_max = prenomSuperieure(prenoms)
    display(nouvelle_liste,resultat,prenoms_max)

main()
