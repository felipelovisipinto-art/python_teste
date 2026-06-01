"""
Clousure e funções que retornam outras funçoes
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"

    return saudar


bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")

for nome in ["Felipe", "Iara", "Minduim"]:
    print(bom_dia(nome))
    print(boa_noite(nome))
