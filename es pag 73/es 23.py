num = int(input("che operazione vuoi eseguire ? (0=somma, 1=sottrazione, 2=moltiplicazione, 3=divisione) "))
n1 = int(input("inserisci il primo numero "))
n2 = int(input("inserisci il secondo numero "))

#def operazioni(num, n1, n2):
#    if(num==0):
#        print(n1+n2)
#    elif(num==1):
#        print(n1-n2)
#    elif(num==2):
#        print(n1*n2)
#    elif(num==3):
#        print(n1/n2)
#
#operazioni(num, n1, n2)

op={0:n1+n2, 1:n1-n2, 2:n1*n2, 3:n1/n2}
print(op[num])
