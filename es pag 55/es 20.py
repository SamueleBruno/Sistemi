
dizionario = {" ": " ", "a" : "b", "b" : "c", "c" : "d", "d" : "e", "e" : "f", "f" : "g", "g" : "h", "h" : "i", "i" : "l", "l" : "m", "m" : "n", "n" : "o", "o" : "p", "p" : "q", "q" : "r", "r" : "s", "s" : "t", "t" : "u", "u" : "v", "v" : "z", "z" : "a"}

parola = input("inserisci una parola ")
stampaCriptato = ""

for lettera in parola : 

    stampaCriptato = stampaCriptato + dizionario[lettera]

print(stampaCriptato)

#for k, v in dizionario.items(): questa riga di codice fa fare un ciclo sul dizionario