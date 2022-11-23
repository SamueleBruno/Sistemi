#leggere le istruzioni da file e farle eseguire a turtle
import turtle

jon=turtle.Turtle()
jon.speed(8)

def istruzioniFile():
    f=open("istruzioni.csv")
    righe=f.readlines()
    f.close()
    jon.begin_fill()
    comandi = {
        "forward": jon.forward,
        "right": jon.right,
        "left": jon.left,
    }

    for riga in righe:
        comado=riga.split(",")
        comandi[comado[0]](int(comado[1]))

    jon.end_fill()
istruzioniFile(jon)
