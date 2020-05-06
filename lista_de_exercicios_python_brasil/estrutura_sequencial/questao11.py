# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo.
# B) a soma do triplo do primeiro com o terceiro. C) o terceiro elevado ao cubo.
x = int(input('Insira um número inteiro: '))
y = int(input('Insira outro número inteiro: '))
z = float(input('Insira um número real: '))

a = ((x * 2) * (y / 2))
int_a = int(a)
b = ((x * 3) + z)
c = (z * z * z)

print('\nRespostas: \nA) ' + str(int_a) + '\nB) ' + str(b) + '\nC) ' + str(c))