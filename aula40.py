""" Calculadora com while """

while True:
    num_1 = input(f'Por favor digite o primeiro numero: ')
    num_2 = input('Por favor digite o segundo numero: ')
    operador = input(f'[+] para somar;\n[-] para subtrair;\n[*] para multiplicação;\n[/] para divisão\n: ')

    numeros_valido = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_valido = True
    except:
        numeros_valido = None

    if numeros_valido is  None:
        print('Um ou ambos os numeros digitados são invalidos')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Calculando, confira a baixo o resultado: ')
    if operador == '+':
      print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)

    if operador == '-':
      print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)

    if operador == '*':
      print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)

    if operador == '/':
      print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)

    sair = input('Digite "sair" para encerrar ou digite qualquer coisa para continuar: ').startswith('sair')

    if sair is True:
        break