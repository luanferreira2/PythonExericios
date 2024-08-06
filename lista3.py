'''
Preencher automaticamente uma lista com todos os números pares
entre 1 e 100 e depois exibir os números para o usuário.
'''

lista = []

numero = 0

while numero <= 100:

    if numero % 2 == 0:

        lista.append(numero)

    numero = numero + 1

print(lista)
