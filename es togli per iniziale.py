l=["Gauss", "Conway", "Eulero", "Hilbert"]

L_GH=[l[i] for i in range(0, 4) if l[i].startswith("G") or l[i].startswith("H")]

print(L_GH)

L_GH=[nome for nome in l if nome[0]=="G" or nome[0]=="H"]

print(L_GH)