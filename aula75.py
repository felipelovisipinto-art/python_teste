# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como paramtro


def criar_multiplicador(multiplicador):
    def calculo(numero):
        return f"{numero} * {multiplicador} = {numero * multiplicador}"

    return calculo


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))
