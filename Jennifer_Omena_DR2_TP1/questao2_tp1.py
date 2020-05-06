ano = int(input('Quantos anos você tem? '))
mes = int(input('Qual mês vocês nasceu? (informe em número) '))
dia = int(input('Qual dia você nasceu? '))

idade_em_dias = dia + (ano*365) + (mes*30)

print('\nSua idade expressa em dias: ' + str(idade_em_dias))