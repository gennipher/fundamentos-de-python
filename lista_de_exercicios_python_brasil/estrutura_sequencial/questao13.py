# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
h = float(input('Informe sua altura: '))
genero = input("Qual seu gênero: ")

peso_homem = (72.7 * h) - 58
peso_mulher = (62.1 * h) - 44.7

if genero == 'F' or genero == 'f' or genero == 'Feminino' or genero == 'feminino':
  print('\nSeu peso ideial é ' + str(round((peso_mulher),2)))
elif genero == 'M' or genero == 'm' or genero == 'Masculino' or genero == 'masculino':
  print('\nSeu peso ideial é ' + str(round((peso_homem),2)))
else:
  print("\nCampo gênero com erro!")