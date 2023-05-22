nome = str(input('Qual é o seu nome? ')).strip()
print('Analisando nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em ninúsculas é {}'.format(nome.lower()))


separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))