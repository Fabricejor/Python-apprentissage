def main():
    # calcul de la moyenne des notes
    note1 = int (input("saisir la note 1: "));
    note2 = int (input("saisir la note 2: "));
    note3 = int (input("saisir la note 3: "));
    result = (note1 + note2 + note3) /3
    print ("la moyenne est de ", result)
    
if __name__ ==  '__main__':
    main()