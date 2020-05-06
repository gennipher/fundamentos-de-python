import turtle

turtle.Screen()
turtle.shape('turtle')

lado = 50
angulo = 90

for i in range(4):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(angulo)
    turtle.forward(lado)


