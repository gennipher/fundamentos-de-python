n = int(input("Vamos calcular fatorial!\n\nDigite o valor de n: "))
 
fatorial = 1

if n == 0:
  fatorial = 1
  print('\nResposta: ' + str(fatorial))
elif n < 0:
  print('\nResposta: Número inválido')
else:
  while (n > 0):
    fatorial = fatorial * n
    n -= 1
  print('\nResposta: ' + str(fatorial))