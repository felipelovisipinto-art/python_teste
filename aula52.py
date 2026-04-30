"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
"""

lista_a = ["Felipe", "Maria"]
lista_b = lista_a


lista_a[0] = "qualquer coisa"
print(lista_b)
