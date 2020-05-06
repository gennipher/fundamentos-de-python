import turtle
ts = turtle.Screen()
turtle.shape('turtle')

lado_quadrado = int(input('Informe o lado do quadrado: '))
lado_triangulo = int(input('Informe o lado do triângulo: '))
raio = int(input('Informe o raio do círculo: '))

def q():
    for i in range(4):
        turtle.forward(lado_quadrado)
        turtle.left(90)

def t():
    for i in range(3):
        turtle.forward(lado_triangulo)
        turtle.left(120)

def c():
    for i in range(360):
        turtle.forward(raio)
        turtle.left(1)

turtle.listen()

ts.onkey(q, 'q')
ts.onkey(t, 't')
ts.onkey(c, 'c')
