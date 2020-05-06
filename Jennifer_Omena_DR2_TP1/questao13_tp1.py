import turtle

turtle.Screen()
turtle.shape('turtle')

n = int(input('Quantos quadrados? '))

# n = 5

x = 0
y = 0
lado = 200
    
for i in range(0, n):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    x = x + 10
    y = y + 10
    lado = lado / 2
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
    