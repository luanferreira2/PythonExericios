'''
Receber 15 números e armazená-los em um vetor.
Ao final, exibir o dobro de cada um dos números.
'''

numero = 0

lista = []

while numero < 15:

    valor = int(input(' Digite um número inteiro: '))

    lista.append(valor)

    numero = numero + 1

print(f' Lista digitada: {lista}')

print(' Valores da lista em dobro:')

for valor in lista:

    print(valor*2, end=', ')

print('\n\t Fim do Programa')