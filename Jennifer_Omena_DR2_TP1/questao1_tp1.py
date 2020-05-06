n = int(input('Informe o último número para a soma: '))
impares = 0
x = 1

while x <= n:
    if x % 2 != 0:
        impares = impares + x
    x = x + 1
    
print('Impares: ' + str(impares))
