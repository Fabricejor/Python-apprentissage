def count_wovels(mots):
    wovels=0
    for i in range (0 , len(mots)-1):
        if mots[i] == "a" or mots[i] == "e" or mots[i] == "u" or mots[i] =="i" or mots[i] == "o":
            wovels+=1
        
    
    return wovels

def main():
    mot = list(input ("Entrez un mot et nous allons compter le nombre de voyels present dedans :"));
    print (mot)
    print( "le nombre de voyeks dans votre mots est de :",count_wovels(mot))
    
    
main()