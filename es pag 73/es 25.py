def isPrimo(x):
    cont =0
    for i in range(1, x+1):
        y=x%i
        if(y==0 or x==1):
            cont+=1
    if(cont == 2 or x==1):
        return True
    else:
        return False
x = int(input("inserisci un numero "))

print(isPrimo(x))
