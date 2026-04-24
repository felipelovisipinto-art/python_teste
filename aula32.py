"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_digitado = input('Digite um número inteiro: ')

# try:
#     numero_int = int(numero_digitado)
#     if numero_int % 2:
#         print(f'O número {numero_int} é ímpar')  
#     else:
#         print(f'O número {numero_int} é par')
# except:
#     print('Valor digitado não é valido')

# if numero_digitado.isdigit():
#     numero_int = int(numero_digitado)
#     resto = numero_int % 2 == 0
#     resultado = 'impar'
#     if resto:
#         resultado = 'par'

#     print(f'O número {numero_int} é {resultado}')
# else:
#     print('Valor digitado não é valido')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

#///////////////////////////////

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite as horas em números interos: ')

# if entrada.isdigit():
#     hora_int = int(entrada)
#     if hora_int in range(0,12):
#         print('Bom dia!')
#     elif hora_int in range(12,18):
#         print('Boa tarde!')
#     elif hora_int in range(18,24):
#         print('Boa noite!')
#     else:
#         print('Horario invalido')
# else:
#     print('Horario invalido')

#///////////////////////////////
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
entrada = input('Porfavor, ensira seu nome: ')

tamanho_nome = len(entrada)

if tamanho_nome > 1:
    if tamanho_nome <= 4 :
        print(f'Seu nome {entrada} é curto e possui {tamanho_nome} caracteres')
    elif tamanho_nome <= 6:
        print(f'Seu nome {entrada} é normal e possui {tamanho_nome} caracteres')
    else:
        print(f'Seu nome {entrada} é muito grande e possui {tamanho_nome} caracteres')
else:
    print('Digite mais de uma letra')
    