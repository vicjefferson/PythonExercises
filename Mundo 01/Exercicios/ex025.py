# Procurando uma string dentro de outra

nome = str(input('Qual é seu nome completo? ')).lower().strip().split()
print(nome)
print('Seu nome tem Silva? ', 'silva' in nome)
