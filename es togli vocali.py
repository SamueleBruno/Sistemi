vocali=['a', 'e', 'i', 'o', 'u']
parola=input("inserisci una parola ")
parolaV=[v for v in parola if not(v in vocali)]
print(parolaV)