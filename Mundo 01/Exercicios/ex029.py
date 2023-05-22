v = int(input('Digite a velocidade do carro: '))

multa = (v - 80) * 7

if v > 80:
  print('\033[31;40mATENÇÃO!!!\033[m')
  print('Você recebeu uma multa por ultrapassar o limite de velocidade de \033[31;40m80km/h\033[31;40m')
  print('Total a pagar é R$ {:.2f}.'.format(float(multa)))
else:
  print('Parabens!!! Não há multas.')