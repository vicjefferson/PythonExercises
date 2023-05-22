n = float(input('Valor 1: '))
s = float(input('Valor 2: '))

op = int(input('''
  QUE OPERAÇÃO DESEJA REALIZAR ?
  [1] SOMAR
  [2] MULTIPLICAR
  [3] MAIOR
  [4] NOVOS NÚMEROS
  [5] SAIR DO PROGRAMA
  -> '''))



while op != 5:
  if op == 1:
    soma = n + s
    print('O valor da sua operação foi {}'.format(soma))
    break
  from time import sleep

n = float(input('Valor 1: '))
s = float(input('Valor 2: '))

maior = 0
soma = n + s
multiplicacao = n * s

print('=-=' * 10)
op = int(input('''
  QUE OPERAÇÃO DESEJA REALIZAR ?
  [1] SOMAR
  [2] MULTIPLICAR
  [3] MAIOR
  [4] NOVOS NÚMEROS
  [5] SAIR DO PROGRAMA
  -> '''))

while op != 5:
  if op > 5:
    print('Opção inválida. Tente novamente')
    op = int(input('''
  QUE OPERAÇÃO DESEJA REALIZAR ?
  [1] SOMAR
  [2] MULTIPLICAR
  [3] MAIOR
  [4] NOVOS NÚMEROS
  [5] SAIR DO PROGRAMA
  -> '''))
  if op == 1:
    print('A soma entre {} e {} é {}'.format(n, s, soma))
    op = int(input('''
      QUE OPERAÇÃO DESEJA REALIZAR ?
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NÚMEROS
      [5] SAIR DO PROGRAMA
      -> '''))
  elif op == 2:
    print('O valor da sua operação foi {}'.format(multiplicacao))
    op = int(input('''
      QUE OPERAÇÃO DESEJA REALIZAR ?
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NÚMEROS
      [5] SAIR DO PROGRAMA
      -> '''))
  elif op == 3:
    if n > s:
      maior = n
      print('O valor 1, {}, é maior'.format(n))
    elif s > n:
      maior = s
      print('O valor 2, {}, é maior'.format(s))
    else:
      print('O valor 1 é igual ao valor 2!')
    op = int(input('''
      QUE OPERAÇÃO DESEJA REALIZAR ?
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NÚMEROS
      [5] SAIR DO PROGRAMA
      -> '''))
  elif op == 4:
    n = float(input('Novo valor 1: '))
    s = float(input('Novo valor 2: '))
    op = int(input('''
      QUE OPERAÇÃO DESEJA REALIZAR ?
      [1] SOMAR
      [2] MULTIPLICAR
      [3] MAIOR
      [4] NOVOS NÚMEROS
      [5] SAIR DO PROGRAMA
      -> '''))

print('Agradecemos por usar nosso programa')

    
