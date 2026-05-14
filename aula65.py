"""
Script: Validador e Formatador de CPF
Autor: Felipe Lovisi Pinto
Data: Maio/2026

Objetivo:
Receber os 9 primeiros dígitos de um CPF, calcular os dois dígitos
verificadores baseados na regra matemática oficial e exibir o
resultado final formatado no padrão (XXX.XXX.XXX-XX).
"""

# Captura o CPF (o fatiamento no laço garante o uso de apenas 9 dígitos)
cpf = input("Digite o os primeiros 9 digitos do seu CPF: ")
soma = 0

# Peso inicial regressivo para o cálculo do 1º dígito
multiplicador = 10

# Itera sobre os 9 primeiros dígitos aplicando a multiplicação da fórmula e acumulando
for digito in cpf[:9]:
    soma += int(digito) * multiplicador
    multiplicador -= 1

# Aplica a matemática final do algoritmo do CPF
multiplicador_10 = soma * 10
divisor_11 = multiplicador_10 % 11

# Se o resto da divisão for maior que 9, o dígito vira 0.
primeiro_digito = divisor_11 if divisor_11 <= 9 else 0
print(f"O primeiro digito do seu cpf é: {primeiro_digito}")

# concatena os 9 digitos com o primeiro digito criado
dez_digitos = cpf[:9] + str(primeiro_digito)

soma_2 = 0
# Peso secundario regressivo para o cálculo do 2º dígito
multiplicador_2 = 11

# Itera sobre os 10 primeiros dígitos aplicando a multiplicação da fórmula e acumulando
for digito in dez_digitos:
    soma_2 += int(digito) * multiplicador_2
    multiplicador_2 -= 1

# Aplica a matemática final do algoritmo do CPF
multiplicador_10 = soma_2 * 10
divisor_11 = multiplicador_10 % 11

# Se o resto da divisão for maior que 9, o dígito vira 0.
segundo_digito = divisor_11 if divisor_11 <= 9 else 0

print(f"O segundo digito do seu cpf é: {segundo_digito}")

cpf_2 = cpf[:9] + str(primeiro_digito) + str(segundo_digito)

print(f"Seu cpf é: {cpf_2[:3]}.{cpf_2[3:6]}.{cpf_2[6:9]}-{cpf_2[9:]}")
