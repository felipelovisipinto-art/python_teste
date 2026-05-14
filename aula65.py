"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
///////////////////////////////////////
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# Captura o CPF (o fatiamento no laço garante o uso de apenas 9 dígitos)
cpf = input("Digite o os primeiros 9 digitos do seu CPF: ")
soma = 0
soma_2 = 0
# Peso inicial regressivo para o cálculo do 1º dígito
multiplicador = 10
# Peso secundario regressivo para o cálculo do º dígito
multiplicador_2 = 11

# Itera sobre os 9 primeiros dígitos aplicando a multiplicação da fórmula e acumulando
for i in cpf[:9]:
    numero = int(i)
    numero *= multiplicador
    soma += numero
    multiplicador -= 1

# Aplica a matemática final do algoritmo do CPF
multiplicador_10 = soma * 10
divisor_11 = multiplicador_10 % 11

# Se o resto da divisão for maior que 9, o dígito vira 0.
primeiro_digito = divisor_11 if divisor_11 <= 9 else 0

print(f"O primeiro digito do seu cpf é: {primeiro_digito}")

# concatena os 9 digitos com o primeiro digito criado
dez_digitos = cpf[:9] + str(primeiro_digito)

# Itera sobre os 10 primeiros dígitos aplicando a multiplicação da fórmula e acumulando
for i in dez_digitos:
    numero = int(i)
    numero *= multiplicador_2
    soma_2 += numero
    multiplicador_2 -= 1

# Aplica a matemática final do algoritmo do CPF
multiplicador_10 = soma_2 * 10
divisor_11 = multiplicador_10 % 11

# Se o resto da divisão for maior que 9, o dígito vira 0.
segundo_digito = divisor_11 if divisor_11 <= 9 else 0

print(f"O segundo digito do seu cpf é: {segundo_digito}")

cpf_2 = cpf[:9] + str(primeiro_digito) + str(segundo_digito)

print(f"Seu cpf é: {cpf_2}")
