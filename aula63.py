# Desempacotamentos em chamadas
# de métodos e funções
string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "python", "é", "legal"
salas = [
    # 0
    [
        "Maria",  # 0
        "Helena",  # 1
    ],
    # 1
    [
        "Elaine",  # 0
    ],
    # 2
    [
        "Luiz",  # 0
        "João",  # 1
        "Eduarda",  # 2
    ],
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print("Maria", "Helena", 1, 2, 3, "Eduarda")
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep="\n")
