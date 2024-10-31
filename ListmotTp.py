# demander a lutisitatuer de donner une phrase 
#si la phrase a moins de 10 mots afficher les 3 premier
# si ellea dis ou plus afficher les 4 dernier mots

phrase = input("Entrez une phrase de votre choix en séparent les mots par un seul espace: ").split(" ")
print ("votre phrase a {}".format(len( phrase)) , "mots")

if len(phrase)<10:
    print (phrase[0:3])
else:
    print (phrase[len(phrase)-4:len(phrase)])
