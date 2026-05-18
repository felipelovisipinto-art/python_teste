import random

cpf = ""
for i in range(9):
    cpf += str(random.randint(0, 9))

soma = 0
# Peso inicial regressivo para o cálculo do 1º dígito
multiplicador = 10

# Itera sobre os 9 primeiros dígitos aplicando a multiplicação da fórmula e acumulando
for digito in cpf:
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

print(cpf_2)
