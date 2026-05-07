"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

lista_compras = []

while True:
    opcao = input("[i]nseirir [a]pagar [l]istar\nDigite: ")

    if opcao == "i":
        adicionar = input("adicionar: ")
        lista_compras.append(adicionar)

    elif opcao == "l":
        for indice, item in enumerate(lista_compras):
            print(f"{indice} {item}")

    elif opcao == "a":
        for indice, item in enumerate(lista_compras):
            print(f"{indice} {item}")

        try:
            deletar = int(input("Escolha o item a ser deletado: "))
            lista_compras.pop(deletar)
        except ValueError:
            print(
                "Não foi possível apagar o indice escolhido, digite um numero inteiro."
            )
        except IndexError:
            print("Primeiro adicione itens a sua lista.")

    else:
        print("Digite um código valido.")
