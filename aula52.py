"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
"""

lista_a = ["Felipe", "Maria", 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = "qualquer coisa"
print(lista_b)
print(lista_a)
