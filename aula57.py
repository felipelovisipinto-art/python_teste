"""
enumerate - enumera iteráveis (índices)
"""

lista = ["Felipe", "Minduim", "Iara", "Jefferson", "Adelia"]
lista.append("joão")

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))
