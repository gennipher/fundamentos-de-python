import turtle

turtle.Screen()
turtle.shape('turtle')

n = int(input('raio: '))

for i in range(360):
    turtle.forward(n)
    turtle.left(1)
    