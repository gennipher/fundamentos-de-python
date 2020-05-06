# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario = int(input('Quanto você ganha por hora? '))
numero_de_horas = int(input('Número de horas por mês: '))

total = salario * numero_de_horas

print('Total do seu salário por mês: R$' + str(total) + ' reais.')