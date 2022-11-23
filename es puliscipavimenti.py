#ogni secondo si muove a caso nelle 4 direzioni di 1 cm, simulare er 2 ore
import turtle
import random

SPEED = 0
SECONDI = 7200

finestra = turtle.Screen()
lista=[0, 90, 180, 270]
pulitore=turtle.Turtle()
pulitore.color(255, 0, 0)
pulitore.speed(SPEED)
for i in range(0, SECONDI):
    a=random.choice(lista)
    pulitore.left(a)
    pulitore.forward(10)


turtle.done()