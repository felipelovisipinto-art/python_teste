"""
Lista de listas e seus índices
"""

i = 0
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

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    i += 1
    print(i)
    for aluno in sala:
        print(aluno)
