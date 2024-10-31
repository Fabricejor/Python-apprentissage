#le juste prix le jouer dois tenter de trouver le chiffre entre 1 et 100
# tant quil ne la pas le jeu continue
# a chaque reponse le system lui notifie si c'est plus ou moins
from random import randint

chifre= randint(1,100)
print ("le chiffre a trouver: ",chifre)
user_answer = int(input ("Jeux du juste prix choisissez un chiffre entre 1 et 100: ")) 

while user_answer != chifre:
    if user_answer < chifre:
        user_answer =int(input("C'est plus :"))
    elif user_answer > chifre:
        user_answer =int(input("c'est moins :"))
if user_answer == chifre:
        print("Bravo vous avez gagnez le chiffre c'etait {}".format(chifre))

