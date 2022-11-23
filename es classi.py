class IPadress():
    def __init__(self, ip_stringa):
        self.ip_notazione_dec = ip_stringa
        self.ip_notazione_bin = self.dec2bin()
        self.ip_binario = self.dec2binNopunti()

    def ip_broadcast(self, subnet_mask='/24'):
        self.ip_binario
        self.dec2bin()
        print()

    def dec2bin(self):
        lista_stringhe = self.ip_notazione_dec.split(".")
        lista_bin=[bin(int (i)) for i in lista_stringhe]
        s=""
        for n in lista_bin:
            temp= str(n)[2 :]
            temp="0"*(8-len(temp)) + temp
            s+=temp+"."

        return s[:-1]

    def dec2binNopunti(self):
        lista_stringhe = self.ip_notazione_dec.split(".")
        lista_bin=[bin(int (i)) for i in lista_stringhe]
        s=""
        for n in lista_bin:
            temp= str(n)[2 :]
            temp="0"*(8-len(temp)) + temp
            s+=temp

        return s[:-1]

    def bin2dec(self):
        pass

    def tolist(self):
        lista_stringhe = self.ip_notazione_dec.split(".")
        return [int(gruppo) for gruppo in lista_stringhe]

def main():
    indirizzoIP=IPadress("192.168.0.123")
    print(indirizzoIP.ip_notazione_dec)
    print(indirizzoIP.tolist())
    print(indirizzoIP.ip_notazione_bin)

if __name__=="__main__":
    main()