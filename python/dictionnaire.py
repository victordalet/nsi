livre_math ={"type":"math","auteur":"Billy", "nombre_de_page": 240, "couleur_dominante":"bleu", "collection":"Nathan"}

def display():
    print("le livre de {}, a été écrit par {}. Il contient {} page et est plutôt {}. Il est édité par {}.".format(livre_math["type"],livre_math["auteur"],livre_math["nombre_de_page"],livre_math["couleur_dominante"],livre_math["collection"]))

def displayPaire():
    print(livre_math.items())

def main():
    display()
    displayPaire()
    liste_livre = [{"type":"math","auteur":"Billy", "nombre_de_page": 240, "couleur_dominante":"bleu", "collection":"Nathan"},
                   {"type":"math","auteur":"Billy", "nombre_de_page": 240, "couleur_dominante":"bleu", "collection":"Nathan"},
                   {"type":"math","auteur":"Billy", "nombre_de_page": 240, "couleur_dominante":"bleu", "collection":"Nathan"}]

main()