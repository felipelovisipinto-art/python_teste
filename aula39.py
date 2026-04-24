<<<<<<< HEAD
"""
Iterando strings com while
"""
#       0123456789...
# nome = 'Felipe Lovisi' #iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[4])

# nova_string = 'F*e*l*i*p*e*L*o*v*i*s*i'

nome = input('Digite seu nome: ')
contador = 0
novo_nome = ''

while contador < len(nome):
   letra = nome[contador]
   novo_nome += letra + '*'
   contador += 1
print(f'Seu novo nome é {novo_nome}')
=======
"""
Iterando strings com while
"""
#       0123456789...
# nome = 'Felipe Lovisi' #iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[4])

# nova_string = 'F*e*l*i*p*e*L*o*v*i*s*i'

nome = input('Digite seu nome: ')
contador = 0
novo_nome = ''

while contador < len(nome):
   letra = nome[contador]
   novo_nome += letra + '*'
   contador += 1
print(f'Seu novo nome é {novo_nome}')
>>>>>>> 8ac0ffb5c4f6b6f52b53bfeee318da2bafe0b586
   