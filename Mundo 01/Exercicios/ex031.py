viagem = int(input('Informe a distância da viagem em km: '))

if viagem <= 200:
  preco = viagem * 0.5
  print('Sua viagem custará um total de R${:.2f}'.format(preco))
else:
  preco = viagem * 0.45
  print('Sua viagem custará um total de R${:.2f}'.format(preco))