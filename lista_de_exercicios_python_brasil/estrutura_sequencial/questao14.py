# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
multa = 4
maximo = 50

peso = float(input("Peso dos peixes: "))

if peso > maximo:
    excesso = peso - maximo
    multa_a_pagar = multa * excesso

print("Você está com excesso de " + str(round(excesso, 2)) + 'kg.')
print("Você deverá pagar R$" + str(round(multa_a_pagar, 2)) + " de multa.")