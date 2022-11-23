class Robot():
    def __init__(self, nome, massa, tipo):
        self.nome = nome#stringa
        self.massa = massa#float
        self.tipo = tipo#stringa

    def getNome(self):
        print(self.nome)

    def isPericoloso(self):
        if self.tipo=="umanoide" and self.massa>=100:
           return True
        else:
            return False

def main():
    rob=Robot("jon", 100, "umanoide")
    rob.getNome()
    if(rob.isPericoloso()):
        print("pericoloso")
    else:
        print("innocuo")

main()