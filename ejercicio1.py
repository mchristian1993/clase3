import turtle
tamaño = int(input('digite el tamaño'))
window = turtle.Screen()
square = turtle.Turtle()

def cuadro (tamaño):
    i=1
    while i <= 4:
        square.forward(tamaño)
        square.left(90)
        i = i + 1
    turtle.mainloop()

cuadro(tamaño)


