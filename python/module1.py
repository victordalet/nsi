import random

a= random.randint(1,100)#choissir le nombre aléatoire

b= int()
c=0 # correspond au compteur d'essaie
while a != b: # boucle
    b= int(input("trouver le bon nombre aléatoire entre 1 et 100"))
    c= +1
    if a < b:
     print("-")
    if a > b:
      print("+")

    else:
          print("nombre trouvée au bout de ", c ,"essaies")





