import turtle

turtle.Screen()
turtle.shape('turtle')
turtle.pencolor('red')

n = int(input('Insira o valor de N: '))
cont = 0

while cont <= n:
    cont += 1
    turtle.forward(cont)
    turtle.left(90)