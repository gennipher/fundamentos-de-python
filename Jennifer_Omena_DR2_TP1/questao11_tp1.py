import turtle

turtle.Screen()
turtle.shape('turtle')

n = int(input('lado: '))

for i in range(3):
    turtle.forward(n)
    turtle.left(120)
    
