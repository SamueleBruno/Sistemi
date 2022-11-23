n = int(input("un numero: "))
lista = [1]*n
lista[0], lista[n-1]=0, 0
print(lista)