#esempi di indicizzazione
s1 = "ciao"
s2 = 'buongiorno'
print(s1[-4])
print(s1[-1])  

print('\n')

#esempi di slicing
#stringa[indice inizio : indice arrivo : gap]
print(s2[1 : 5])
print(s2[1 : 5 : 2])
print(s2[: 4]) #se ometto il primo parte comunque da 0
print(s2[3 :]) #se ometto il secondo va dall'indice di inizio fino in fondo
print(s2[: -1])

r = len(s2) #restituisce la lunghezza della stringa
print(r)

var = input("frase: ") #input
int(var) #cambia il tipo di una variabile
float(var) #cambia il tipo di una variabile

 