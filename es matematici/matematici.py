def leggifile():
    file = open("file.csv")
    righe=file.readlines()
    file.close()
    diz = {"id":[], "nome":[]}
    for riga in righe:
        campiRiga=riga[:-1].split(",")
        diz["id"].append(int(campiRiga[0]))
        diz["nome"].append(campiRiga[1][1:])
    return diz

def nomeId(id, diz):
    listaId = diz["id"]
    listaNomi = diz["nome"]
    for i, n in zip(listaId, listaNomi):
        if i == id:
            return n

def main():
    diz=leggifile()
    id = 2
    nome = nomeId(id, diz)
    print(nome)

if __name__=="__main__":
    main()