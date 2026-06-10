# Exercicio - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for enunciado in perguntas:
    print(f"{enunciado['Pergunta']}\n")

    for indice, alternativa in enumerate(enunciado['Opções']):
        print(f"{indice}) {alternativa}")


    resposta = input(f'Escolha a opções correta: ')

    escolha_final = int(resposta)
    opcao_escolhida = enunciado['Opções'][escolha_final]

    if opcao_escolhida == enunciado['Resposta']:
            print(f'\nCerta resposta!👍')
            acertos +=1
    else:
         print(f'Resposta errada! ❌\n')
print(f'Parabens! voce acertou {acertos} de {len(perguntas)} perguntas')