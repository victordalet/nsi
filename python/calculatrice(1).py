# initialiasation des variables : premier nombre; opérateur
number_one = int(input("Ton nombre : "))
operator = input("Ton opérateur :  +   ;   -   ;   /   ;   *   ;   **   ;   !   : ")

# si on ne rentre pas une factorielle, on demande un deuxième nombre
if operator!="!":
    number_two = int(input("Ton nombre : "))

# si l'addition est selectionnée
if operator == "+":
    calcul = number_one + number_two
    print("{} + {} = {}".format(number_one, number_two, calcul))

# si la soustraction est selectionnée
elif operator == "-":
    calcul = number_one - number_two
    print("{} - {} = {}".format(number_one, number_two, calcul))

# si la multiplication est selectionnée
elif operator == "*":
    calcul = number_one * number_two
    print("{} x {} = {}".format(number_one, number_two, calcul))

# si la division est selectionnée
elif operator == "/":
    # tant que le dénominateur = 0
    while number_two == 0:
        print("Le dénominateur doit être différent de 0")
        number_two = int(input("Ton nombre (différent de  0) : "))
    calcul = number_one / number_two
    print("{} / {} = {}".format(number_one, number_two, calcul))

# si la puissance est selectionnée
elif operator == "**":
    calcul = number_one ** number_two
    print("{} ** {} = {}".format(number_one, number_two, calcul))



# si la factorielle est selectionnée
elif operator == "!":
    # intialisation pour la factorielle
    calcul = 1
    facto = number_one
    while facto > 1:
        calcul = calcul*facto
        facto -= 1
    print("{}! = {}".format(number_one, calcul))

# si aucun de ces opérateurs est selectionné
else:
    print("Opérateur incorrect")
