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
    # 0       1       2          0  1   2   3   4
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)],  # 2
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])
