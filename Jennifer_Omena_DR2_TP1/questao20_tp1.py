import turtle

turtle.Screen()
turtle.shape('turtle')
turtle.pencolor('red')
turtle.speed('fastest')

n = int(input('Insira o valor de N para somar ao angulo: '))
cont = 0

while cont <= 200:
    cont += 1
    turtle.forward(cont)
    turtle.left(90+n)