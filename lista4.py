'''
Receber números do usuário para preencher uma lista de 10 posições,
porém, só é permitido armazenar no vetor números positivos
(repetir até que as 10 posições da lista estejam preenchidas).
No final, exiba a lista.
'''

lista = []

numero = 0

valor = int(input(' Digite um número inteiro:'))

soma = 0

while numero < 10:

    if valor >= 0:

        lista.append(valor)

        numero = numero + 1

    else:

        print(' O número digitado deve ser positivo.')

    valor = int(input(' Digite um número inteiro:'))

print(f' Lista: \n {lista}')

