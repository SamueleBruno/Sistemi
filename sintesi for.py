def main():
    lista1 = ["a", "b", "c", "d"]
    lista2 = [1, 2, 3, 4]
    
#for su lista1 c style
#for su lista1 python style
#for su lista1 con enumerate
#for su lista1 e lista2 python style (zip)
#for su lista1 e lista2 c style (range)

    diz = {"lettere": lista1, "numeri": lista2}
    print("\nC style:")

    for indice in range(len(lista1)):
        print(lista1[indice])

    print("\npython style:")

    for indice in lista1:
        print(indice)

    print("\ncon enumerate:")

    for i, valore in enumerate(lista1):
        print(i, valore)

    print("\ncon zip:")

    for i, j in zip(lista1, lista2):
        print(i, j)

    print("\nC style di due liste:")

    for i in range(len(lista1)):
        print(lista1[i], lista2[i])

#for su diz usando items()
#for su diz senza items()

    print("\ndizionario con items")

    

if __name__ == "__main__":
    main()
