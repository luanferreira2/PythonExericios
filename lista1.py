'''
Receber 12 números e armazená-los em uma lista.
Ao final, exibir a quantidade de números negativos e positivos informados'''

numero = 0

lista = []

contadorP = 0

contadorN = 0

while numero < 12:

    valor = int(input(' Digite um número inteiro: '))

    lista.append(valor)

    numero = numero + 1

for valor in lista:

    if valor >= 0:

        contadorP = contadorP + 1

    else:

        contadorN = contadorN + 1

print(f' A quantidade de número positivos na lista é igual a {contadorP}')

print(f' A quantidade de número negativos na lista é igual a {contadorN}')

print('\t Fim do Programa')