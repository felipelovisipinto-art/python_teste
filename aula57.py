"""
enumerate - enumera iteráveis (índices)
"""

lista = ["Felipe", "Minduim", "Iara"]
lista.append("joão")

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)
