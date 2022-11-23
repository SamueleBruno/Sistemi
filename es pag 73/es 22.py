num = int(input("inserisci un numero "))

def VerificaDiv(num):
    if((num%3)==0):
        print("il numero è divisibile per 3")
    if((num%5)==0):
        print("il numero è divisibile per 5")
    if((num%2)==0):
        print("il numero è divisibile per 2")

VerificaDiv(num)