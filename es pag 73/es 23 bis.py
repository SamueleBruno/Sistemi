#fare un programma che prende due numeri a cui fa una delle quattro operazioni a caso
#rand int (0, 3)
import random

num = random.randint(0, 3)
print(num)
n1 = int(input("inserisci il primo numero "))
n2 = int(input("inserisci il secondo numero "))

op={0:n1+n2, 1:n1-n2, 2:n1*n2, 3:n1/n2}

print(op[num])