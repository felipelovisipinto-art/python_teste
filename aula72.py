# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplicador(3, 5, 5, 7)
print(resultado)

# Crie uma função que fale se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


numero_digitado = input("Escolha um número: ")


def impar_par(x):
    numero = int(x) % 2 == 0
    if numero:
        return f"{numero_digitado} é par"
    return f"{numero_digitado} é impar"


resultado_2 = impar_par(numero_digitado)
print(resultado_2)
