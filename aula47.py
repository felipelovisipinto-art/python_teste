"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

tentativas = 0
palavra_secreta = "Minduim"
letra_acertada = ""
letra_digitada = ""

while True:
    os.system("cls")

    letra_digitada = input("\nDigite a primeira letra:")

    if len(letra_digitada) != 1:
        print("\nPorfavor digite apenas uma letra por vez.")
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ""

    for i in palavra_secreta:

        if i in letra_acertada:
            palavra_formada += i

        else:
            palavra_formada += "*"

    tentativas += 1
    print(f"\nSeu gabarito atual é: {palavra_formada}\n{tentativas} tentativa(s).")
    if palavra_formada == palavra_secreta:
        print(
            f'\nPARANÉNS, voce venceu o jogo!\nA palavra secreta era: "{palavra_secreta}" e voce precisou de {tentativas} tentavias para vencer.'
        )
        letra_acertada = ""
        tentativas = 0
        continue
