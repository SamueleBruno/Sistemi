import turtle
finestra = turtle.Screen()


gianni= turtle.Turtle()

dizpos={3:(0, 10), 4: (-180, 10), 5:(180 , 10), 6: (360, 10)}

def poligono(x, y, numlati, gianni):
    gianni.speed(10)
    gianni.color("black")
    gianni.begin_fill()
    gianni.penup()
    gianni.setpos(x, y)
    gianni.pendown()
    lato=360/numlati
    angolo=360/numlati
    for _ in range(0, numlati):
        gianni.left(angolo)
        gianni.forward(lato)
    gianni.end_fill()

for numlati, posizione in dizpos.items():
    poligono(posizione[0], posizione[1], numlati, gianni)

turtle.done()