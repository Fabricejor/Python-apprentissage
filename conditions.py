# code
wallet = 5000
computer_price = 8000

# Conditions de test de comparaison
if (wallet > computer_price) and (wallet <1000):
    print("solde suffisant")
else:
    print("solde insuffisant , vousn'avez que {} XOF" .format(wallet))
    
#condition ternaires
test = ("votre solde apres cette transaction est de "+ str(wallet-computer_price),"Solde insuffisant il vous manque " +str(computer_price-wallet))[wallet>computer_price]
print(test)