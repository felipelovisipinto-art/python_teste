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
"""

# Coleta os primeiros 9 digitos do cpf, porem tambem aceita o cpf inteiro.
cpf = input("Digite o os primeiros 9 digitos do seu CPF: ")

# seta a variavel soma igual a 0, variavel essa que será responsavel por armazenar a soma e multiplicação dos nove digitos.
soma = 0

# multiplicador é a variavel responsavel por realizar a multiplicação dos digitos, indo de 10 ate 2.
multiplicador = 10

# laço responsavel por pegar os nove digitos do cpf e realizar primeiro a conversão do cpf de string para int, realizar a multiplicação do digito;
#  somar para dar o resultado da primeiira etapa.
for i in cpf[:9]:
    numero = int(i)
    numero *= multiplicador
    soma += numero
    multiplicador -= 1

# etapa onde o resultado obitido no loop será multiplicado por 10.
multiplicador10 = soma * 10

# etapa onde a multiplicação feita a cima é dividida por 11.
divisor11 = multiplicador10 % 11

# Variavel responsavel por verificar se o primeiro digito encontrado é maior ou menor que 9, caso seja maior que 9 o resultado é setado como 0.
primeiro_digito = divisor11 if divisor11 < 10 else 0

# Resultado do primeiro digito do cpf encontrado.
print(f"O primeiro digito do seu cpf é: {primeiro_digito}")
