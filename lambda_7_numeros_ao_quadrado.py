"""
Dada uma lista de números inteiros, use uma função lambda em conjunto com map() para criar uma nova
lista onde cada número é elevado ao quadrado.

Instruções:

    Crie uma lista de números inteiros.
    Use a função map() em conjunto com uma função lambda para elevar cada número ao quadrado.
    Converta o resultado de map() em uma lista e imprima a nova lista.

numeros = [1, 2, 3, 4, 5]
"""

numeros = [1, 2, 3, 4, 5]

numeros_quadrados = list(map(lambda numero: numero ** 2, numeros))

print(numeros_quadrados)
