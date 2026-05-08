"""
Lista de listas e seus índices
"""

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
    ["Luiz", "João", "Eduarda", (0, 2, 3, 4)],  # 0  # 1  # 2
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
