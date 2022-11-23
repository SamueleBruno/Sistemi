def tabellaPitagorica():
    return [[numero * indice for numero in range(1, 11)] for indice in range(1, 11)]

def scrivifile(tabella):
    file=open("tabella pitagorica.txt", "w")
    for i in tabella:
        file.write(f"\t{i}\n")
    file.close()





def main():
    tabella= tabellaPitagorica()
    print(tabella)
    scrivifile(tabella)

if __name__ == "__main__":
    main()