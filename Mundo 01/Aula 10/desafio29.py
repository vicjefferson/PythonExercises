v = int(input('Digite a velocidade do carro: '))

multa = (v - 80) * 7

if v > 80:
  print('Você recebeu uma multa por ultrapassar o limite de velocidade de 80km/h')
  print('Total a pagar é R$ {:.2f}.'.format(float(multa)))
else:
  print('Parabens!!! Não há multas.')