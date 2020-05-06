# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
F = int(input('Temperatura em Farenheit: '))

C = (5*(F-32)/9)
int_C = int(C)

print(str(F) + 'ºF em ºC vale: ' + str(int_C) + 'ºC.')