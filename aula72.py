# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função que fale se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplicador(3, 5, 5, 7)
print(resultado)


numero_digitado = input("Escolha um número: ")


def impar_par(x):
    numero = int(x)
    if numero % 2 == 0:
        return "Par"

    else:
        return "Impar"


resultado_2 = impar_par(numero_digitado)
print(f"O seu numero {numero_digitado} é {resultado_2}")
