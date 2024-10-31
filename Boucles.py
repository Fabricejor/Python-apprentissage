print("Vous etes le client n*1")
print("Vous etes le client n*2")
print("Vous etes le client n*3")
print("Vous etes le client n*4")
print("Vous etes le client n*5")

#for
for num_client in range(0,5):
    print("vous etes le cient n*{}".format(num_client+1))
#for each ; pour chaque client
emails = ["Fabricejordan@gmail.com", "Jordan@gmail.com", "Ramos@gmail.com"]
# for Elemens in Ensembles 
blacklist =["Jordan@gmail.com", "Ramos@gmail.com"]
for email in emails:
    if email in blacklist:
        print("Envoie impossible {} cet email ne figure pas dans la base de donnés" .format(email))
    else:
        print("Emails envoyé à {}".format(email))