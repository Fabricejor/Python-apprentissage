#l'age d'une personne et lui proposer du popcorn en fonction de ses renformations
user_age = int(input ("quel est votre age ?"))
total_price=0

if user_age <= 0:
    print("Age invalide")
elif 1<=user_age <18:
    total_price=7
    print("voici le tarif des mineurs", total_price , "$")
elif user_age>=18:
    total_price=12
    print("voici le tarif des normal", total_price , "$")
    
    
    
popcorn=input("Vous souhaitez ajouter du popcorn?(tapez Oui ou Yes ) ")
if popcorn == "Yes" or popcorn == "Oui":
        total_price=total_price+5
        print("voici le total du prix à payer :" ,total_price,"$")
        
else :
        print("voici le total du prix à payer :" ,total_price,"$")