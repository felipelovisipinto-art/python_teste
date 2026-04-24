primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
                    
if primeiro_valor > segundo_valor:
    print(f'O numero {primeiro_valor} é maior que o numero {segundo_valor}')

elif segundo_valor > primeiro_valor:
    print(f'O numero {segundo_valor} é maior que o numero {primeiro_valor}')

elif primeiro_valor == segundo_valor:
    print(f'O numero {primeiro_valor} é iguai ao {segundo_valor}')