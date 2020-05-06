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