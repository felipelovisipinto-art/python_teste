"""
enumerate - enumera iteráveis (índices)
"""

lista = ["Felipe", "Minduim", "Iara"]
lista.append("joão")

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# for indice, nome in enumerate(lista):
#     print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
