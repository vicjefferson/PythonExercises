from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
while op != 5:
  print('''
  QUE OPERAÇÃO DESEJA REALIZAR ?
  [1] SOMAR
  [2] MULTIPLICAR
  [3] MAIOR
  [4] NOVOS NÚMEROS
  [5] SAIR DO PROGRAMA''')
  op = int(input('Informe sua opção: '))
  if op == 1:
    print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
  elif op == 2:
    print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
  elif op == 3:
    maior = 0
    if n1 > n2:
      maior = n1
      print('{} é o maior entre os dois.'.format(maior))
    elif n2 > n1:
      maior = n2
      print('{} é o maior entre os dois.'.format(maior))
    else:
      print('{} e {} são iguais.'.format(n1, n2))
  elif op == 4:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
  elif op > 5:
    print('Opção inválida. Tente novamente.')
  sleep(1)
print('Fim do programa. Volte sempre!')