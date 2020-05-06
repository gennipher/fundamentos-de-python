n = int(input("Vamos calcular fatorial!\n\nDigite o valor de n: "))

resultado = 1

if n < 0:
  print('Resposta: Número inválido!')
else:
  for i in range(1, n+1):
      resultado *= i
  print('\nResposta: ' + str(resultado))
