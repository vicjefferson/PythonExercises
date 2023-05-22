nome = input('Qual é o seu nome?  ')
print('Prazer em te conhecer, {:20}!'.format(nome)) #Victor em 20 caracteres
print('Seu nome fica assim: {:>20}!'.format(nome)) #Victor à direita,em 20 caracteres
print('Seu nome fica assim: {:<20}!'.format(nome)) #Victor à esquerda, em 20 caracteres
print('Seu nome fica assim: {:^20}!'.format(nome)) #Victor centralizado, em 20 espaços
print('Seu nome fica assim: {:=^20}!'.format(nome)) #Victor centralizado entre =, em 20 espaços
