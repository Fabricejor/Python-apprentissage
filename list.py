# import statistics
from statistics import mean
from random import shuffle
#creer une liste qui va stocker des pseudo
list =["Falou","Ibrahima","Jordan", "Jean"]
print (list)
print (list[0])
print (list[len(list)-1])
#modif d'un elements de la liste
list[0]='Kaizen'
# ajouter un element à une position donné
list.insert(2,"Ramos" )
print ("Liste modifié" , list)


print ("Liste selectione" , list[2:4])
# ajouter un element a la fin dune liste 
list.append("Jujutsu")
print(list)
list.extend(["saison1","saison2"])
print(list)
#supprimer des elements de la list
del list[0] #supprime kaisen
list.pop(0)#suprimera Ibrahima vu que sa ete placé en premier apres la supressio de kaisen
list.remove("saison1")
print(list)
# supprime tous
list.clear()
print("Liste supprimé",list)

notes =[ 9, 10, 20 ,
        6 ,15 ,18]
print (notes)
#note melangé
shuffle(notes)
print(notes)
#module statisctic
# results = statistics.mean(notes)
results = mean(notes)
print("La moyennes des notes est de {}".format(results) )