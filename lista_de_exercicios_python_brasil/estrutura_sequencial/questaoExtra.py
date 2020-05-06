x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

maior = menor = x

if (y > maior):
    maior = y

if (z > maior):
    maior = z

if (y < menor):
    menor = y

if (z < menor):
    menor = z

print('Menor: ', menor)
print('Maior: ', maior)