#fare un dizionario che fa da rubrica telefonica
rubrica = {"basso" : 1, "jon" : 2}

nuovoContatto = input("inserisci il nuovo contatto ")
rubrica[nuovoContatto] = 3

print(rubrica[nuovoContatto])