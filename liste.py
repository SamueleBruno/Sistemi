#liste, tuple, dizionari permettono di salvare più variabili in una struttura dati

l = [1, 2, 3, 4] #lista

print(l) #stampa la lista

print(l[0]) #per stampare il primo elemento

print(l[1 : 3]) #stampa gli elementi 2 e 3

print(l[: : -1]) #stampa la lista al contrario

#le liste sono mutabili
l[1]= 9 
print(l)

l.append(5) #append è un metodo per aggiungere un elemento ad una lista
print(l)