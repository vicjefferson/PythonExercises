import random
import time

print('''
--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--
Vou pensar em um número entre 0 e 5. Tente adivinhar...
--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--
''')

num = (input('Em que número pensei? '))
print('PROCESSANDO...')
time.sleep(3)

numbers = [0, 1, 2, 3, 4, 5]
escolhindo = random.choice(numbers)

if escolhindo == numbers:
  print('PARABÉNS! Você conseguiu me vencer!')
else:
  print('GANHEI! Pensei no número {} e não no {}'.format(escolhindo, num))
