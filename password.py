#video playlist ytb exo sur mdp
password = input("Entrez votre mot de passe :")
password_lengh = len(password)
print (password_lengh)

if password_lengh < 8 :
    print ("Mot de passe trop court!")
elif 8 < password_lengh <= 12:
    print ("Mot de passe moyen.")
else :
    print ("mot de passe valide")