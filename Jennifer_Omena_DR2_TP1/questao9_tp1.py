import math
import turtle
 
tupla = ()
    
x = float(input("Informe o lado x\n"))
y = float(input("Informe o lado y\n"))
z = float(input("Informe o lado z\n"))

tupla += (x,y,z)
print(tupla)

if (x < y+z and y < x+z and z < y+x):
  print("Forma triangulo")
else:
  print("Nao forma triangulo")

if ( x==y and y==z) :
  print("Triângulo Equilátero")
elif (x==y or y==z or x==z) :
  print("Triângulo Isoceles")
else:
  print("Triângulo Escaleno")

def q(numero):
  return (numero*numero)

# Calcular os ângulos
angulo_z = math.acos( (q(x) + q(y) - q(z)) / (2 * x * y));
angulo_x = math.acos( (q(y) + q(z) - q(x)) / (2 * y * z));
angulo_y = 3.14 - angulo_x - angulo_z ;
# Converter de radianos para graus e de ângulo interno para ângulo externo
angulo_z = 180 - (180 / 3.14 * angulo_z);
angulo_x = 180 - (180 / 3.14 * angulo_x);
angulo_y = 180 - (180 / 3.14 * angulo_y);

turtle.showturtle()
turtle.forward(x)
turtle.left(angulo_z)
turtle.forward(y)
turtle.left(angulo_x)
turtle.forward(z)
    