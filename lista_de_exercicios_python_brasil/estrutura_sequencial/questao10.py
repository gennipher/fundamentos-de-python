# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
C = int(input('Temperatura em Celsius: '))

F = ((C * 9 / 5) + 32)
int_F = int(F)

print(str(C) + 'ºC em ºF vale: ' + str(int_F) + 'ºF.')