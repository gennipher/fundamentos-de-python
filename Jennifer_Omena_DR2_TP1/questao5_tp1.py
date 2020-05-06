# Primeira função

print('Letra A)\n')
frutas = ('pera','uva','banana','morango')
elemento = input("Digite o nome de uma fruta: ").lower()

if(frutas.__contains__(elemento)):
    index = frutas.index((elemento))
    print('\n', elemento, 'está na tupla, é o índice', index, '\n')
else:
    print('\n', elemento, 'não está na tupla\n')


# Segunda função

print('Letra B)\n')
print(f'\n Primeira metade da Tupla: {frutas[0:2]}, Segunda metade da Tupla: {frutas[2:4]}\n\n')


# Terceira função

print('Letra C)\n')
print('0 - pera\n1 - uva\n2 - banana\n3 - morango\n')

eliminar = int(input('Digite o número da fruta que você deseja eliminar da lista?'))

tuplaAuxiliar = ()

if(eliminar < 0 or eliminar > 3):
    print('Essa fruta não existe')
else:
    for x in range(0,4):
        if(x != eliminar):
            tuplaAuxiliar += (frutas[x],)

print(tuplaAuxiliar)


# Quarta função

print('\nLetra D)\n')
print(frutas[::-1])