text = input("Entrez une chaine de type (Email Pseudo  motdepasse)").split(" ")
print (text)
print ("Bienvenue {} voici ton email {}".format(text[1], text[0]))