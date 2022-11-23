#richiedi 2 numeri, un dizionario fa la media aritmetica, l'altro la media geometrica

n1 = int(input("inserisci il primo numero : "))
n2 = int(input("inserisci il secondo numero : "))

media= {"aritmetica" : (n1 + n2)/2 , "geometrica" : (n1*n2)**0.5}

g = input("media geometrica o aritmetica ? ")

print(media[g])