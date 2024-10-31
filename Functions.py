def welcome():
    print ("Welcome new player")
    results = 5+6
    print("Le résultats du calcul {}".format(results))
    
    
# welcome()

def next_year():
    global year
    print ("Nous sommes actuellement en  " ,year )
    year+=1
    
    
year= 2018

next_year()