import random

num = int(input('Qual número o Pc está pensando entre 0 e 5 -> '))
numeros = [0,1,2,3,4,5]
escolhido = random.choice(numeros)
if num == escolhido:
  print('Parabéns, você acertou!')
else:
  print('Que pena, você errou!')
  print('O número correto era {}'.format(escolhido))