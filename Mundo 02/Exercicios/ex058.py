from random import randint
print('-=-' * 10)
print('   JOGO DA ADVINHAÇÃO   ')
print('-=-' * 10)
pc = randint(0, 10)
player = int(input('Tente adivinhar qual número estou pensando: '))
tentativas = 1

while player != pc:
  player = int(input('Errado! Tente novamente: '))
  tentativas += 1
print('Você acertou o número correto após {} tentativas.'.format(tentativas))
