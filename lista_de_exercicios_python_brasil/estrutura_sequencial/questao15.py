# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto.
# quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos
# e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto   : R$
# - IR (11%)        : R$
# - INSS (8%)       : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.              : Salário Bruto - Descontos = Salário Líquido.

salario = float(input('Quanto você ganha por hora? '))
numero_de_horas = int(input('Número de horas trabalhadas no mês? '))

salario_bruto = salario * numero_de_horas

print('\nTotal do seu salário por mês: R$' + str(round(salario_bruto,2)))

ir = salario_bruto - (salario_bruto-0.11)
inss = salario_bruto - (salario_bruto-0.08)
sindicato = salario_bruto - (salario_bruto-0.05)

salario_liquido = salario_bruto - ir - inss - sindicato

print('Salário Líquido: R$' + str(round(salario_liquido,2)))