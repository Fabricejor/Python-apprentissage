#fonction qui retourne le maximum

def maximum (n,m):
    print("le maximum des deux nombres est")
    return print (" ",max(n,m))

def main():
    n= int(input("Entrez le premier nombre: "))
    m= int(input("Entrez le premier nombre: "))
    maximum(n,m)

main()