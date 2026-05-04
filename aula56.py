"""
Tipo tupla - Uma lista imutável
"""

nomes = "Felipe", "Minduim", "Iara"
nomes[1] = "outro"
_, _, nome, *resto = nomes
print(nomes)
print(nome)
