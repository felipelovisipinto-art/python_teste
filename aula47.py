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

tentativas = 0
palavra_secreta = "Minduim"
letra_acertada = ""
letra_digitada = ""

while True:
    letra_digitada = input(
        "Para começar o jogo, tente adivinhar a palavra secreta.\n Digite a primeira letra:"
    )

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada
